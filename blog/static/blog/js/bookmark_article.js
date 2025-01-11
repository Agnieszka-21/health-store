$(document).ready(function(){
    $('.bookmark-article').click(
        function(e) {
            let article_id = $(this).attr('data-article-item');
            let that = $(this);
            let icon = that.find('.fa-bookmark');
            let icon_classlist_value = icon[0].classList.value;
            var csrftoken = Cookies.get('csrftoken');
            let action_url = 'reading-list/';

            $.ajax({
                url: action_url,
                type: 'POST',
                data: {'article_id': article_id, 'icon_classlist_value': icon_classlist_value },
                headers : { 'X-CSRFToken': csrftoken},
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
    )
})
