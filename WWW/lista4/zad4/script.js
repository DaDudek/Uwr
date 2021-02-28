var actuall = 0;
var counter = 0;

function openRemoveDialog(button){
    actuall = button.data("row");
    $("#dialog-confirm").dialog("open");
}

$( function() {
    var dialog, form,
        name = $( "#name" ),
        email = $( "#email" ),
        password = $( "#password" ),
        allFields = $( [] ).add( name ).add( email ).add( password );

    function addUser() {
        allFields.removeClass( "ui-state-error" );
        let firstName = $( "#firstName" );
        let lastName  = $( "#lastName" );
        let city = $("#city");
        let postCode = $("#postCode")
        let birthDate = $("#birthDate").val()
        let betterBirthDate = birthDate.split("-").reverse().join("-")

        $( "#users tbody" ).append( "<tr data-row='"+ counter +"'>" +
            "<td>" + firstName.val() + "</td>" +
            "<td>" + lastName.val() + "</td>" +
            "<td>" + city.val() + "</td>" +
            "<td>" + postCode.val() + "</td>" +
            "<td>" + betterBirthDate + "</td>" +
            "<td><button class='removeDialogBtn' onclick='openRemoveDialog($(this))' data-row='"+ counter +"'>remove</button></td>" +
            "</tr>" );
        counter = counter + 1;
        dialog.dialog( "close" );
        return false;
    }

    dialog = $( "#dialog-form" ).dialog({
        autoOpen: false,
        height: 400,
        width: 350,
        modal: true,
        buttons: {
            "Create an account": addUser,
            Cancel: function() {
                dialog.dialog( "close" );
            }
        },
        close: function() {
            form[ 0 ].reset();
            allFields.removeClass( "ui-state-error" );
        }
    });

    form = dialog.find( "form" ).on( "submit", function( event ) {
        event.preventDefault();
        addUser();
    });

    $( "#create-user" ).button().on( "click", function() {
        dialog.dialog( "open" );
    });






    $( function() {
        $( "#dialog-confirm" ).dialog({
            resizable: false,
            height: "auto",
            width: 400,
            modal: true,
            autoOpen: false,
            buttons: {
                "Delete items": function() {
                    $("tr[data-row='"+actuall+"']").remove();
                    $( this ).dialog( "close" );
                },
                Cancel: function() {
                    $( this ).dialog( "close" );
                }
            }
        });
    } );





} );
