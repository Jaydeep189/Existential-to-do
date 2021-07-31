//$('#trigger').click(function(){
//    $("#form-question").css("display", "flex");
//});

$('#submit-main').on('click', function () {
    $.ajax({
        type: 'POST',
        url: '/echo/html/',
        data: {
            html: '<form id="form_foo"><textarea></textarea><input type="submit"></input></form>',
            delay: 1,
        },
        success: function (data, textStatus, jqXHR) {
            $('#submit-main').find('.modal-body').html(data);
            $('#submit-main').modal('show');
        },
    });
});

// Handle submit.  Here we return an error regardless of the
// input given:
$("#submit-main").on('submit', '#form_foo', function (e) {
    $.ajax({
        type: 'POST',
        url: '/echo/html/',
        data: {
            html: '<form id="form_foo_2"><span class="error">You must write something silly here:</span><textarea></textarea><input type="submit"></input></form>',
            delay: 0,
        },
        success: function (data, textStatus, jqXHR) {
            $('#submit-main').find('.modal-body').html(data);
        },
    });
    e.preventDefault();
    return false;
});

// Handle second submit.  Here we close the modal.
// In a real application you can use the status to determine
// which action to take (success or redisplay the form).
$("#submit-main").on('submit', '#form_foo_2', function (e) {
    alert('Thanks for writing something silly.  Closing modal');
    $('#submit-main').modal('hide');
    e.preventDefault();
    return false;
});