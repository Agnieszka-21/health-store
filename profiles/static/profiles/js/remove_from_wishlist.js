$(document).ready(function(){
    $('.add-to-wishlist').click(
        function(e) {
                let product_id = $(this).attr('data-product-item');
                let that = $(this);
                let wishlist_product = that.parents('.wishlist-product');
                var csrftoken = Cookies.get('csrftoken');
                let action_url_remove = `${product_id}/remove/`;

                $.ajax({
                    url: action_url_remove,
                    type: 'POST',
                    data: {'attr_id': product_id },
                    headers : {'X-CSRFToken': csrftoken},
                    success: function (result) {
                        wishlist_product[0].classList.add('d-none');
                    },   
            });
        }
    );
});
