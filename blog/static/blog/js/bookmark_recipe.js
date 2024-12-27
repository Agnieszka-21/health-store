$(document).ready(function(){
    $('.bookmark-recipe').click(
        function(e) {
            let recipe_id = $(this).attr('data-recipe-item');
            console.log('article_id: ', recipe_id);

            let that = $(this);
            console.log('that - recipe: ', that);

            let icon = that.find('.fa-bookmark');
            console.log('bookmark icon - recipe: ', icon);

            let icon_classlist_value = icon[0].classList.value;
            console.log('icon_classlist_value bookmark - recipe: ', icon_classlist_value);

            var csrftoken = Cookies.get('csrftoken');
            console.log('csrftoken bookmark: ', csrftoken);
            let action_url = 'fav-recipe-list/';

            $.ajax({
                url: action_url,
                type: 'POST',
                data: {'recipe_id': recipe_id, 'icon_classlist_value': icon_classlist_value },
                headers : { 'X-CSRFToken': csrftoken},
                success: function (result) {
                    console.log('Success');
                    if (icon[0].classList.contains('fa-regular')) {
                        console.log('Icon contains fa-regular');
                        icon[0].classList.remove('fa-regular');
                        icon[0].classList.add('fa-solid');
                    } else if (icon[0].classList.contains('fa-solid')) {
                        icon[0].classList.remove('fa-solid');
                        icon[0].classList.add('fa-regular');
                    }
                },
                error: function() {
                    console.log('An error occurred - recipe bookmarking went wrong...');
                }    
            });
        }
    )
})
