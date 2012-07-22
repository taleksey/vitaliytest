$(document).ready(function(){
    $('#id_yearbook, #id_birthday, #id_dieday').datepicker({ dateFormat: "yy-mm-dd" });
    $('#confirm-delete').click(function(e) {
        e.preventDefault();
        $('#myModal').modal({ backdrop: true })
        
    });
});
