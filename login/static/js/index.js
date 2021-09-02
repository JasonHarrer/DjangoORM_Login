$(document).ready(function() {
    $("#register_first_name").keyup(validate_form)
    $("#register_last_name").keyup(validate_form)
    $("#register_email").keyup(validate_form)
    $("#register_email").keyup(validate_email)
    $("#register_password1").keyup(validate_form)
    $("#register_password2").keyup(validate_form)
})


function validate_form() {
    console.log("validate form")
    var okay = true

    if($("#register_first_name").val().length < 2)                     { okay == false }
    if($("#register_last_name").val().length < 2)                      { okay == false }
    if($("#register_email").val().length < 5)                          { okay == false }
    if($("#error_register_email").is(":visible"))                      { okay == false }
    if($("#register_password1").val().length < 8)                      { okay == false }
    if($("#register_password2").val().length < 8)                      { okay == false }
    if($("register_password1").val() != $("register_password2").val()) { okay == false }

    if(okay) { $("#register_submit").disabled = false }
    else     { $("#register_submit").disabled = true  }
}


function validate_email() {
    console.log("validate email")
   $.ajax('/api/login/validate_email').done(function(response) {
        if(response.exists) {
            $("#error_register_email").text("An account using this email address already exists.  If this is yours, please log in instead.")
            $("#error_register_email").show()
        } else {
            $("#error_register_email").hide() 
        }
   })
}

function validate_passwords() {
    console.log("validate passwords")
}
