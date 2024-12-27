$(document).ready(function(){
    $('.remove-recipe').click(
        function(e) {
                let recipe_id = $(this).attr('data-recipe-item');
                let that = $(this);
                let bookmarked_recipe = that.parents('#recipe-list');
                var csrftoken = Cookies.get('csrftoken');
                let action_url_remove = `${recipe_id}/remove-recipe-bookmark/`;

                $.ajax({
                    url: action_url_remove,
                    type: 'POST',
                    data: {'recipe_id': recipe_id },
                    headers : { 'X-CSRFToken': csrftoken},
                    success: function (result) {
                        console.log('Success');
                        bookmarked_recipe[0].classList.add('d-none');
                    },
                    error: function() {
                        console.log('An error occurred');
                    }    
            });
        }
    )
})
