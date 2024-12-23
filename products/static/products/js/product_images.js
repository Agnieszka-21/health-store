$(document).ready(function() {
    $('#img-thumbnail-1').click(function(){

        let thumbSrc = $(this).attr('src');
        let thumbAlt = $(this).attr('alt');
        let mainSrc = $('#main-image').attr('src');
        let mainAlt = $('#main-image').attr('alt');

        $('#main-image').attr({'src': thumbSrc});
        $('#main-image').attr({'alt': thumbAlt});
        $('#img-thumbnail-1').attr({'src': mainSrc});
        $('#img-thumbnail-1').attr({'alt': mainAlt});
    });

    $('#img-thumbnail-2').click(function(){
        
        let thumbSrc = $(this).attr('src');
        let thumbAlt = $(this).attr('alt');
        let mainSrc = $('#main-image').attr('src');
        let mainAlt = $('#main-image').attr('alt');

        $('#main-image').attr({'src': thumbSrc});
        $('#main-image').attr({'alt': thumbAlt});
        $('#img-thumbnail-2').attr({'src': mainSrc});
        $('#img-thumbnail-2').attr({'alt': mainAlt});
    });
});