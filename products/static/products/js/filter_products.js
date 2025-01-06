//Filter products based on their category for all products on the shop page

// Code in this file has been written based on sort_products.js (which was copied from Code Institute's
// walkthrough project Boutique Ado)

$('#category-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        currentUrl.searchParams.set("category", selectedVal);
        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("category");
        window.location.replace(currentUrl);
    }
});
