function changeData(method, arguments) {
  $.getJSON(
    "/background_process_test",
    { updateFunction: method, arguments },
    function (newValue) {
      $(".updatable > .value_" + method).each(function (idx) {
        $(this).text(newValue);
      });
    }
  );
  return false;
}
