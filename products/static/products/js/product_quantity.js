// Code copied and adjusted from Code Institute's walkthrough project Boutique Ado

    // Disable +/- buttons outside 1-9 range
    function handleEnableDisable(itemId) {
        let currentValue = parseInt($(`.id_qty_${itemId}`).val());
        let minusDisabled = currentValue < 2;
        let plusDisabled = currentValue > 8;
        $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all quantity inputs on page load
    let allQtyInputs = $('.qty_input');
    for(let i = 0; i < allQtyInputs.length; i++){
        let itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time a quantity input is changed
    $('.qty_input').change(function() {
        let itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity of a specific product
    $('.increment-qty').click(function(e) {
       e.preventDefault();
       let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       let currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue + 1);
       let itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });

    // Decrement quantity of a specific product
    $('.decrement-qty').click(function(e) {
       e.preventDefault();
       let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       let currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue - 1);
       let itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });