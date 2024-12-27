$(document).ready(function(){
    $('.bookmark-article').click(
        function(e) {
            let article_id = $(this).attr('data-article-item');
            console.log('article_id: ', article_id);

            // let slug = $(this).attr('data-article-slug');

            let that = $(this);
            console.log('that - article: ', that);

            let icon = that.find('.fa-bookmark');
            console.log('bookmark icon: ', icon);

            let icon_classlist_value = icon[0].classList.value;
            console.log('icon_classlist_value bookmark: ', icon_classlist_value);

            var csrftoken = Cookies.get('csrftoken');
            console.log('csrftoken bookmark: ', csrftoken);
            let action_url = 'reading-list/';

            $.ajax({
                url: action_url,
                type: 'POST',
                data: {'article_id': article_id, 'icon_classlist_value': icon_classlist_value },
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
                    console.log('An error occurred - bookmarking went wrong...');
                }    
            });
        }
    )
})
