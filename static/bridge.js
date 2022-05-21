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

function routerNavigate(router, targetPath) {
  $.ajax({
    type: "GET",
    url: "/background_process_test",
    data: { router, path: targetPath },
    success: function (response) {
      const { path, body } = JSON.parse(response);
      history.pushState({ router, path: targetPath }, "", path);
      $(".router_" + router).html(body);
    },
    error: function (err) {
      console.log(err);
    },
  });
  return false;
}

var pageRouter;

function setPageRouter(name) {
  if (!pageRouter) {
    pageRouter = {};
    pageRouter.name = name;
  } else {
    pageRouter.child = { name };
  }

  console.log(pageRouter);
}

addEventListener("popstate", function (event) {
  let path = "/";
  let router = pageRouter.name;
  if (event.state) {
    path = event.state.path;
    router = event.state.router;
  }

  $.ajax({
    type: "GET",
    url: "/background_process_test",
    data: { router: router, path: path },
    success: function (response) {
      const { body } = JSON.parse(response);
      $(".router_" + router).html(body);
    },
    error: function (err) {
      console.log(err);
    },
  });
});

$(function () {
  $("div[onload]").trigger("onload");
});
