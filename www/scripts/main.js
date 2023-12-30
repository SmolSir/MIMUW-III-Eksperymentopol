///////////////////
//   ENDPOINTS   //
///////////////////

const LOGGER = true;

const FILTERS_ENDPOINT = "http://127.0.0.1:5000/backend/available_filters?";
const EXPERIMENTS_ENDPOINT = "";

function print(content) {
    if (LOGGER) {
        console.log(content);
    }
}

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
