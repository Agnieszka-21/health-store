$(document).ready(function(){
    $('.add-to-wishlist').click(
        function(e) {
                let product_id = $(this).attr('data-product-item');
                let that = $(this);
                let wishlist_product = that.parents('#wishlist-product');
                var csrftoken = Cookies.get('csrftoken');
                let action_url_remove = `${product_id}/remove/`;

                console.log('Product id is: ', product_id);
                console.log('That is: ', that);
                console.log('wishlist_product: ', wishlist_product[0]);
                console.log('CSRF: ', csrftoken)
                console.log('Action URL remove: ', action_url_remove);

                $.ajax({
                    url: action_url_remove,
                    type: 'POST',
                    data: {'attr_id': product_id },
                    headers : { 'X-CSRFToken': csrftoken},
                    success: function (result) {
                        console.log('Success');
                        wishlist_product[0].classList.add('d-none');
                    },
                    error: function() {
                        console.log('An error occurred');
                    }    
            });
        }
    )
})
