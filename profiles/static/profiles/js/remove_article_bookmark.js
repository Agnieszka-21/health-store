$(document).ready(function(){
    $('.remove-article').click(
        function(e) {
                let article_id = $(this).attr('data-article-item');
                let that = $(this);
                let bookmarked_article = that.parents('#reading-list');
                var csrftoken = Cookies.get('csrftoken');
                let action_url_remove = `${article_id}/remove-article-bookmark/`;

                console.log('Article id is: ', article_id);
                console.log('That (article) is: ', that);
                console.log('bookmarked_article: ', bookmarked_article[0]);
                console.log('CSRF: ', csrftoken)
                console.log('Action URL remove: ', action_url_remove);

                $.ajax({
                    url: action_url_remove,
                    type: 'POST',
                    data: {'article_id': article_id },
                    headers : { 'X-CSRFToken': csrftoken},
                    success: function (result) {
                        console.log('Success');
                        bookmarked_article[0].classList.add('d-none');
                    },
                    error: function() {
                        console.log('An error occurred');
                    }    
            });
        }
    )
})
