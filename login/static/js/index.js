$(document).ready(function() {
    $("#register_first_name").keyup(validate_register_form)
    $("#register_last_name").keyup(validate_register_form)
    $("#register_email").keyup(validate_register_form)
    $("#register_password1").keyup(validate_register_form)
    $("#register_password2").keyup(validate_register_form)
})


async function validate_register_form() {
    console.log("validate form")
    var okay = true

    if(!validate_register_first_name())      { okay = false }
    console.log("okay = " + okay)
    if(!validate_register_last_name())       { okay = false }
    console.log("okay = " + okay)
    if(!validate_register_email())           { okay = false }
    console.log("okay = " + okay)
    let exists = await validate_register_email_exists()
    console.log("exists = " + exists)
    if(!exists)                              { okay = false }
    console.log("okay = " + okay)
    if(!validate_register_password1())       { okay = false }
    console.log("okay = " + okay)
    if(!validate_register_password2())       { okay = false }
    console.log("okay = " + okay)
    if(!validate_register_passwords_match()) { okay = false }
    console.log("okay = " + okay)

    if(okay) { console.log("okay = true");  $("#register_submit").attr("disabled", false) }
    else     { console.log("okay = false"); $("#register_submit").attr("disabled", true)  }
}


function validate_register_first_name() {
    if (($("#register_first_name").val().length < 2)  ||
        ($("#register_first_name").val().length > 50)) {
        $("#error_register_first_name").show()
        console.log("validate first name failed")
        return false
    } else {
        console.log("validate first name passed")
        $("#error_register_first_name").hide()
        return true
    }

}


function validate_register_last_name() {
    if (($("#register_last_name").val().length < 2) ||
        ($("#register_last_name").val().length > 50)) {
        $("#error_register_last_name").show()
        console.log("validate last name failed")
        return false
    } else {
        $("#error_register_last_name").hide()
        console.log("validate last name passed")
        return true
    }
}


function validate_register_email() {
    if (($("#register_email").val().length < 2) ||
        ($("#register_email").val().length > 50)) {
        $("#error_register_email").show()
        console.log("validate email failed")
        return false
    } else {
        $("#error_register_email").hide()
        console.log("validate email passed")
        return true
    }
}


async function validate_register_email_exists() {
    response = await $.ajax('/api/login/validate_email/' + $('#register_email').val())
    console.log(response)
    if(response.exists) {
        $("#error_register_email_exists").show()
        console.log("validate email does not exist failed")
        return false
    } else {
        console.log("validate email does not exist passed")
        $("#error_register_email").hide()
        return true
    }
}


function validate_register_password1() {
    if (($("#register_password1").val().length < 8)   ||
        ($("#register_password1").val().length > 100)) {
        $("#error_register_password1").show()
        console.log("validate password1 failed")
        return false
    } else {
        $("#error_register_password1").hide()
        console.log("validate password1 passed")
        return true
    }
}


function validate_register_password2() {
    if (($("#register_password2").val().length < 8)   ||
        ($("#register_password2").val().length > 100)) {
        $("#error_register_password2").show()
        console.log("validate password2 failed")
        return false
    } else {
        $("#error_register_password2").hide()
        console.log("validate password2 passed")
        return true
    }
}


function validate_register_passwords_match() {
    var okay = true

    if(($("#register_password1").val().length < 8) ||
       ($("#register_password2").val().length < 8)) {
            // Don't enable button, but don't show error, either
            $("#error_register_passwords_match").hide()
            console.log("validate passwords match failed due to passwords not being long enough")
            return false
    } else {
        if($("register_password1").val() != $("register_password2").val()) {
            $("#error_register_passwords").show()
            console.log("validate passwords match failed")
            return false
        } else {
           $("#error_register_passwords").hide()
            console.log("validate passwords match passed")
           return true
        }
    }
}
