$(document).ready(function(){
    $('.add-to-wishlist').click(
        function(e) {
            let product_id = $(this).attr('data-product-item');
            let that = $(this);
            let icon = that.find('.fa-heart');
            let icon_classlist_value = icon[0].classList.value;
            let csrftoken = Cookies.get('csrftoken');
            let action_url_2 = `${product_id}/add-to-wishlist/`;

            $.ajax({
                url: action_url_2,
                type: 'POST',
                data: {'attr_id': product_id, 'icon_classlist_value': icon_classlist_value },
                headers : {'X-CSRFToken': csrftoken},
                success: function (result) {
                    if (icon[0].classList.contains('fa-regular')) {
                        icon[0].classList.remove('fa-regular');
                        icon[0].classList.add('fa-solid');
                    } else if (icon[0].classList.contains('fa-solid')) {
                        icon[0].classList.remove('fa-solid');
                        icon[0].classList.add('fa-regular');
                    }
                },   
            });
        }
    );
});