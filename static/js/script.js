$(document).ready( function() {


function getLoginForm(evt) {

    if (evt) {
        evt.preventDefault();
    }

    alert("French Fries!");

}

function getSignUpForm(evt) {

    if (evt) {
        evt.preventDefault();
    }

    alert("Macaroni Salad!");

}

$('#login').click(getLoginForm);
$('#signup').click(getSignUpForm);

});