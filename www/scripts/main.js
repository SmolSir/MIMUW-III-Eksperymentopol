///////////////////
//   ENDPOINTS   //
///////////////////

const LOGGER = true;

const FILTERS_ENDPOINT = "./backend/available_filters?";
const EXPERIMENTS_ENDPOINT = "";

function print(content) {
    if (LOGGER) {
        console.log(content);
    }
}


///////////////////////////////
//   SINGLE ENTRY BUILDERS   //
///////////////////////////////

function buildCategoryInput(id, name, state) {
    const categoryInput = document.createElement("input");

    categoryInput.type = "checkbox";
    categoryInput.classList.add("btn-check");
    categoryInput.id = "category_checkbox_" + id.toString();
    categoryInput.autocomplete = "off";

    print(categoryInput);

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

function buildItemList(itemRecords) {
    const itemList = document.getElementById("item_list_not_checked");
    var itemChildrenList = [];

    for (const [id, name] of itemRecords) {
        const item = buildItem(id, name, false);
        itemChildrenList.push(item);
    }

    itemList.replaceChildren(...itemChildrenList);
}


/////////////////////////
//   FETCH FUNCTIONS   //
/////////////////////////
async function fetchAvailableFilters() {
    var filters;
    var request = await fetch(
        FILTERS_ENDPOINT,
        {
            method: "GET"
        }
    );

    filters = await request.json();

    print(filters);

    return filters.error ? -1 : filters;
}
