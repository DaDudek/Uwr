const accountNumber = document.getElementById('accountNumber');
accountNumber.addEventListener('focusout', (event) => {
    accountNumberValidation();
});

const pesel = document.getElementById('pesel');
pesel.addEventListener('focusout', (event) => {
    peselValidation();
});

const date = document.getElementById('date');
date.addEventListener('focusout', (event) => {
    dateValidation();
});

const email = document.getElementById('email');
email.addEventListener('focusout', (event) => {
    emailValidation();
});

const submit = document.getElementById('submit');
submit.addEventListener('click', (event) => {
    validation();
});


function accountNumberValidation()
{
    let accountPattern = new RegExp(/^\d{2}$/);
    let accountValue = document.getElementById("accountNumber").value;
    if(!accountPattern.test(accountValue))
    {
        alert("Account number must have 26 digits and no other characters");
    }
}

function peselValidation()
{
    let peselPattern = new RegExp(/^\d{11}$/);
    let peselValue = document.getElementById("pesel").value;
    if(!peselPattern.test(peselValue))
    {
        alert("Pesel must have 11 digits and no other characters");
    }
}

function dateValidation()
{
    let datePattern = new RegExp(/^\d{4}([-]\d{2}){2}$/);
    let dateValue = document.getElementById("date").value;
    if(!datePattern.test(dateValue))
    {
        alert("Dates must look like dd.mm.rrrr");
    }
}

function emailValidation()
{
    //regex based on stackoverflow rfc2822 implementation
    let emailPattern = new RegExp(/[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/);
    let emailValue = document.getElementById("email").value;
    if(!emailPattern.test(emailValue))
    {
        alert("Wrong email address");
    }
}


function validation()
{
    accountNumberValidation();
    peselValidation();
    dateValidation();
    emailValidation();
}


