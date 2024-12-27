$(document).ready(function(){
    $('.share-link').click(
        function(e) {
            let confirmation = $('.confirmation-text')[0];
            // Get page url and copy it to clipboard
            current_url = window.location.href;
            navigator.clipboard.writeText(current_url);
            // Show confirmation that the link has been copied to the clipboard
            confirmation.classList.add('d-inline-block');
            confirmation.classList.remove('d-none');
        }
    )
})