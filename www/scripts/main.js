///////////////////
//   ENDPOINTS   //
///////////////////

const FILTERS_ENDPOINT = "../../backend/available_filters";
const EXPERIMENTS_ENDPOINT = "";

async function buildCategoryInput(id, name, state) {
    const category_input = document.createElement("input");

    category_input.type = "checkbox";
    category_input.classList.add("btn-check");
    category_input.id = "category_checkbox_" + id.toString();
    category_input.autocomplete = "off";

    return category_input;
}

async function buildCategoryLabel(id, name, state) {
    const category_label = document.createElement("label");

    category_label.classList.add("btn")

}

async function buildCategoryList(categoryList) {
    const categoryList = document.getElementById("category_list");
}

async function fetchFilters() {
    var filters;
    var request = await fetch(
        FILTERS_ENDPOINT,
        {
            method: "GET"
        }
    );

    filters = await request.json();
    return filters.error ? -1 : filters;
}
