///////////////////
//   ENDPOINTS   //
///////////////////

const LOGGER = true;

const FILTERS_ENDPOINT = "/api/available_filters";
const EXPERIMENTS_ENDPOINT = "";

function print(content) {
    if (LOGGER) {
        console.log(content);
    }
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


//////////////////////////////
//   COMPARISON FUNCTIONS   //
//////////////////////////////

function compareItems(itemA, itemB) {
    var itemLabelA = itemA.querySelector('label').textContent;
    var itemLabelB = itemB.querySelector('label').textContent;

    return itemLabelA.localeCompare(itemLabelB);
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

    const itemListChecked = document.getElementById("item_list_checked");
    const itemListNotChecked = document.getElementById("item_list_not_checked");

    const itemList =
        Array.from(itemListChecked.children).concat(Array.from(itemListNotChecked.children));

    const itemListCheckedUpdate = itemList.map(deepClone).filter(itemChecked).sort(compareItems);
    const itemListNotCheckedUpdate = itemList.map(deepClone).filter(itemNotChecked).sort(compareItems);

    itemListChecked.replaceChildren(...itemListCheckedUpdate);
    itemListNotChecked.replaceChildren(...itemListNotCheckedUpdate);
}
