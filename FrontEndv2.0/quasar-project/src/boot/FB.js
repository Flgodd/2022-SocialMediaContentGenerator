export function InitSDK(appID,version) {
  return new Promise(resolve => {
    window.fbAsyncInit = function () {
      FB.init({
        appId:appID,
        xfbml: false,
        version:version,
        cookie: true
      });
    };
    FB.getLoginStatus(({ authResponse }) => {
      if (authResponse) {
        accountService.apiAuthenticate(authResponse.accessToken).then(resolve);
      } else {
        resolve();
      }
    });

    (function (d, s, id) {
      const fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) { return; }
      const js = d.createElement(s); js.id = id;
      js.src = '//connect.facebook.net/en_US/sdk.js';
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
  });
}

export function FBLogin() {
  return new Promise(resolve => {
    window.FB.login(response => resolve(response));
  });
}
export function FBLogout() {
  return new Promise(resolve => {
    window.FB.logout(response => resolve(response));
  });
}
