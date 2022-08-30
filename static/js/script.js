$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#exampleModal .modal-content").html("");
        $("#popup-messages-content").html("");
        $("#exampleModal").modal("show");
      },
      success: function (data) {
        $("#exampleModal .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#exampleModal").modal("hide");
          $("#popup-messages-content").html(data.message_list);
        }
        else {
          $("#exampleModal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Send email
  $("button.btn.btn-primary").click(loadForm);
  $("#exampleModal").on("submit", saveForm);

});