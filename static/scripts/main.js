///////////////////
//   ENDPOINTS   //
///////////////////

const ENDPOINT_PREFIX = "/api";
const FILTERS_ENDPOINT = ENDPOINT_PREFIX + "/available_filters";
const EXPERIMENTS_ENDPOINT = ENDPOINT_PREFIX + "/search";


//////////////////////////
//   HELPER FUNCTIONS   //
//////////////////////////

function compareByNth(A, B, n) {
    return A[n - 1].localeCompare(B[n - 1]);
}

function compareByField(A, B, field) {
    return A[field].localeCompare(B[field]);
}


/////////////////////////
//   QUERY FUNCTIONS   //
/////////////////////////

function buildExperimentsQuery(categoryIdList, itemIdList) {
    function extractCategoryId(string) {
        return "category" + "=" + string.match(/\d+$/)[0];
    }

    function extractItemId(string) {
        return "item" + "=" + string.match(/\d+$/)[0];
    }

    const querySeparator = "&";

    var categoriesQuery = categoryIdList.map(extractCategoryId).join(querySeparator);
    var itemsQuery = itemIdList.map(extractItemId).join(querySeparator);

    const queryEntry = categoriesQuery || itemsQuery ? "?" : "";

    const query = queryEntry + categoriesQuery + querySeparator + itemsQuery;

    return query.replace(/&+$/, ""); // Remove trailing &s
}

function processExperimentsQuery(urlSearchParams) {
    function getIdListByKey(params, key) {
        return params
            .getAll(key)
            .map(value => parseInt(value))
            .filter(value => !isNaN(value));
    }

    const categoryIdList = getIdListByKey(urlSearchParams, "category");
    const itemIdList = getIdListByKey(urlSearchParams, "item");

    categoryIdList.forEach(id =>
        document.getElementById(`category_checkbox_${id}`).checked = true);

    itemIdList.forEach(id =>
        document.getElementById(`item_checkbox_${id}`).checked = true);

    updateItemList();
}


/////////////////////////
//   FETCH FUNCTION   //
/////////////////////////

async function fetchData(request) {
    return fetch(request, { method: "GET" })
        .then(response => response.json())
        .catch(error => Promise.reject(error));
}


///////////////////////////////
//   INTERACTIVE FUNCTIONS   //
///////////////////////////////

window.onload = async function init() {
    var currentUrl = new URL(window.location.href);

    await fetchData(FILTERS_ENDPOINT)
        .then(({ categories, items }) => {
            categories.sort((categoryA, categoryB) => compareByNth(categoryA, categoryB, 2));
            items.sort((itemA, itemB) => compareByNth(itemA, itemB, 2));

            buildCategoryList(categories);
            buildSuggestionList(items);
            buildItemList(items);
        })
        .catch(error => {
            console.error("Failed to fetch data: ", error);
        });

    var experimentsRequest = EXPERIMENTS_ENDPOINT + "?" + currentUrl.searchParams.toString();
    processExperimentsQuery(currentUrl.searchParams);

    await fetchData(experimentsRequest)
        .then(experimentsJson => {
            var experiments = experimentsJson.experiment_list;

            experiments.sort(
                (experimentA, experimentB) => compareByField(experimentA, experimentB, "title")
            );

            buildExperimentList(experiments);
        })
        .catch(error => {
            console.error("Failed to fetch data: ", error);
        });
}

function markItemChecked(item) {
    function markItemCheckbox(itemCheckbox) {
        var checkbox = itemCheckbox.querySelector('.form-check-input');
        var label = itemCheckbox.querySelector('.form-check-label');

        if (label.textContent.trim().localeCompare(item, undefined, { sensitivity: "accent" }) === 0) {
            checkbox.checked = true;
            return true;
        }

        return false;
    }

    var itemListChecked = document.querySelectorAll('#item_list_checked .form-check');
    var itemListNotChecked = document.querySelectorAll('#item_list_not_checked .form-check');
    var itemFound = false;

    itemListChecked.forEach(function(itemCheckbox) {
        itemFound |= markItemCheckbox(itemCheckbox);
    });

    itemListNotChecked.forEach(function(itemCheckbox) {
        itemFound |= markItemCheckbox(itemCheckbox);
    });

    return itemFound;
}

var itemSearchInput = document.getElementById("item_search");

itemSearchInput.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        if (markItemChecked(itemSearchInput.value.trim())) {
            // Successfully marked item as checked
            itemSearchInput.value = "";
        }
        // Failed to mark item as checked
    }
})

itemSearchInput.addEventListener('change', function(event) {
    if (markItemChecked(itemSearchInput.value.trim())) {
        // Successfully marked item as checked
        itemSearchInput.value = "";
    }
    // Failed to mark item as checked
})

var experimentSearchApplyButton = document.getElementById("experiment_search_apply_button");
var experimentSearchResetButton = document.getElementById("experiment_search_reset_button");

experimentSearchApplyButton.addEventListener('click', updateExperimentList);
experimentSearchResetButton.addEventListener('click', resetExperimentList);

///////////////////////////////
//   SINGLE ENTRY BUILDERS   //
///////////////////////////////

function buildCategoryInput(id, name, state) {
    const categoryInput = document.createElement("input");

    categoryInput.type = "checkbox";
    categoryInput.classList.add("btn-check");
    categoryInput.id = "category_checkbox_" + id.toString();
    categoryInput.autocomplete = "off";

    return categoryInput;
}

function buildCategoryLabel(id, name, state) {
    const categoryLabel = document.createElement("label");

    categoryLabel.classList.add("btn");
    categoryLabel.classList.add("btn-outline-primary");
    categoryLabel.classList.add("flex-fill");
    categoryLabel.classList.add("m-1");
    categoryLabel.setAttribute("for", "category_checkbox_" + id.toString());
    categoryLabel.textContent = name;

    return categoryLabel;
}

function buildSuggestion(id, name, state) {
    const itemOption = document.createElement("option");

    itemOption.value = name.toString();

    return itemOption;
}

function buildItem(id, name, state) {
    const item = document.createElement("div");
    const itemInput = document.createElement("input");
    const itemLabel = document.createElement("label");

    itemInput.classList.add("form-check-input");
    itemInput.type = "checkbox";
    itemInput.value = "";
    itemInput.id = "item_checkbox_" + id.toString();

    itemLabel.classList.add("form-check-label");
    itemLabel.setAttribute("for", "item_checkbox_" + id.toString());
    itemLabel.textContent = name;

    item.classList.add("form-check");
    item.appendChild(itemInput);
    item.appendChild(itemLabel);

    return item;
}

function buildExperimentImagePart(imagePath) {
    const experimentImageContainer = document.createElement("div");
    const experimentImage = document.createElement("img");

    experimentImage.classList.add("rounded");
    experimentImage.classList.add("img-fluid");
    experimentImage.classList.add("mb-2");
    experimentImage.classList.add("mb-lg-0");
    experimentImage.src = imagePath;

    experimentImageContainer.classList.add("col-lg-4");
    experimentImageContainer.classList.add("col-md-5");
    experimentImageContainer.classList.add("col-md");
    experimentImageContainer.appendChild(experimentImage);

    return experimentImageContainer;
}

function buildExperimentTextPart(id, shortDescription, title) {
    const experimentTextContainer = document.createElement("div");
    const experimentTextHeader = document.createElement("h3");
    const experimentVideoLink = document.createElement("a");
    const experimentDescription = document.createElement("p");

    const experimentVideoLinkPrefix = "./experiment?id=";

    experimentDescription.textContent = shortDescription;

    experimentVideoLink.classList.add("stretched-link");
    experimentVideoLink.href = experimentVideoLinkPrefix + id.toString();
    experimentVideoLink.textContent = title;

    experimentTextHeader.appendChild(experimentVideoLink);

    experimentTextContainer.classList.add("col");
    experimentTextContainer.appendChild(experimentTextHeader);
    experimentTextContainer.appendChild(experimentDescription);

    return experimentTextContainer;
}

function buildExperiment(id, imagePath, shortDescription, title) {
    const experiment = document.createElement("div");
    const experimentContainer = document.createElement("div");

    experimentContainer.classList.add("row");
    experimentContainer.classList.add("position-relative");
    experimentContainer.appendChild(buildExperimentImagePart(imagePath));
    experimentContainer.appendChild(buildExperimentTextPart(id, shortDescription, title));

    experiment.classList.add("experiments-list-item");
    experiment.classList.add("mb-3");
    experiment.appendChild(experimentContainer);

    return experiment;
}


/////////////////////////////
//   LIST ENTRY BUILDERS   //
/////////////////////////////

function buildCategoryList(categoryRecords) {
    const categoryList = document.getElementById("category_list");
    var categoryChildrenList = [];

    for (const [id, name] of categoryRecords) {
        const categoryInput = buildCategoryInput(id, name, false);
        categoryChildrenList.push(categoryInput);

        const categoryLabel = buildCategoryLabel(id, name, false);
        categoryChildrenList.push(categoryLabel);
    }

    categoryList.replaceChildren(...categoryChildrenList);
}

function buildSuggestionList(itemRecords) {
    const suggestionList = document.getElementById("item_search_suggestion_list");
    var suggestionChildrenList = [];

    for (const [id, name] of itemRecords) {
        const suggestion = buildSuggestion(id, name, false);
        suggestionChildrenList.push(suggestion);
    }

    suggestionList.replaceChildren(...suggestionChildrenList);
}

function buildItemList(itemRecords) {
    document.getElementById("item_list_checked").innerHTML = "";
    const itemList = document.getElementById("item_list_not_checked");
    var itemChildrenList = [];

    for (const [id, name] of itemRecords) {
        const item = buildItem(id, name, false);
        itemChildrenList.push(item);
    }

    itemList.replaceChildren(...itemChildrenList);
}

function buildExperimentList(experimentRecords) {
    const experimentList = document.getElementById("experiment_list");
    var experimentChildrenList = [];

    for (const {id, image_path, short_description, title} of experimentRecords) {
        const experiment = buildExperiment(id, image_path, short_description, title);
        experimentChildrenList.push(experiment);
    }

    experimentList.replaceChildren(...experimentChildrenList);
}


//////////////////////////
//   ITEM LIST UPDATE   //
//////////////////////////

function updateItemList() {
    function deepClone(node) {
        return node.cloneNode(true);
    }

    function itemChecked(node) {
        var checkbox = node.querySelector('input[type="checkbox"]');
        return checkbox && checkbox.checked;
    }

    function itemNotChecked(node) {
        var checkbox = node.querySelector('input[type="checkbox"]');
        return checkbox && !checkbox.checked;
    }

    function compareItems(itemA, itemB) {
        var itemLabelA = itemA.querySelector('label').textContent;
        var itemLabelB = itemB.querySelector('label').textContent;

        return itemLabelA.localeCompare(itemLabelB);
    }

    const itemListChecked = document.getElementById("item_list_checked");
    const itemListNotChecked = document.getElementById("item_list_not_checked");

    const itemList =
        Array.from(itemListChecked.children).concat(Array.from(itemListNotChecked.children));

    const itemListCheckedUpdate = itemList.map(deepClone).filter(itemChecked).sort(compareItems);
    const itemListNotCheckedUpdate = itemList.map(deepClone).filter(itemNotChecked).sort(compareItems);

    itemListChecked.replaceChildren(...itemListCheckedUpdate);
    itemListNotChecked.replaceChildren(...itemListNotCheckedUpdate);
}


////////////////////////////////
//   EXPERIMENT LIST UPDATE   //
////////////////////////////////

async function updateExperimentList() {
    const originUrl = new URL(window.location.origin);

    updateItemList();

    const categoryIdList = Array
        .from(document.querySelectorAll('#category_list input[type="checkbox"]:checked'))
        .map(category => category.id);

    const itemIdList = Array
        .from(document.querySelectorAll('#item_list_checked input[type="checkbox"]:checked'))
        .map(item => item.id);

    const query = buildExperimentsQuery(categoryIdList, itemIdList);

    var experimentsRequest = EXPERIMENTS_ENDPOINT + query;

    await fetchData(experimentsRequest)
        .then(experimentsJson => {
            var experiments = experimentsJson.experiment_list;

            experiments.sort(
                (experimentA, experimentB) => compareByField(experimentA, experimentB, "title")
            );

            buildExperimentList(experiments);
        })
        .catch(error => {
            console.error("Failed to fetch data: ", error);
        });

    window.history.replaceState(null, null, originUrl.href + query);
}

function resetExperimentList() {
    document.querySelectorAll('#category_list input[type="checkbox"]')
        .forEach(checkbox => checkbox.checked = false);

    document.querySelectorAll('#item_list_checked input[type="checkbox"]')
        .forEach(checkbox => checkbox.checked = false);

    document.querySelectorAll('#item_list_not_checked input[type="checkbox"]')
       .forEach(checkbox => checkbox.checked = false);

    updateExperimentList();
}
