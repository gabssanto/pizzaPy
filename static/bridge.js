function changeData(method, arguments) {
  $.getJSON(
    "/handleDOM",
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
    url: "/handleDOM",
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
    url: "/handleDOM",
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

$(document).on('keyup', 'input', function(e) {
  // Does some stuff and logs the event to the console
  console.log('input changed', e.target.value)
});

// var limit = 10; //your input limit
// $(document).on('ready',function(){
//     var oldValue = $( "input[type='text']" ).val();
//     $( "input[type='text']" ).on('keydown',function(e) {
//         oldValue = $( this ).val();
//     })
//     $( "input[type='text']" ).on('input propertychange',function(e) {
//         newValue = $(this).val();
//         if(newValue.length > limit){
//             $(this).val(oldValue);
//             alert('String too long.');
//         }
//     });
// });
