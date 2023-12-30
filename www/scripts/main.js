///////////////////
//   ENDPOINTS   //
///////////////////

const CATEGORY_LIST_ENDPOINT = "";
const ITEM_LIST_ENDPOINT = "";
const EXPERIMENT_LIST_ENDPOINT = "";

async function buildCategory(category, state) {
    const category_button = document.createElement('button');
    category_button.type = 'button';
    category_button.classList.add('btn');
    category_button.classList.add('btn-primary');

    category_button.textContent = category;
    category_button.disabled = state;

    return category_button;
}

async function fetchCategoryList() {
    var category_list;
    var request = await fetch(
        CATEGORY_LIST_ENDPOINT,
        {
            method: 'GET'
        }
    );

    category_list = await request.json();
    return category_list.error ? -1 : category_list;
}
