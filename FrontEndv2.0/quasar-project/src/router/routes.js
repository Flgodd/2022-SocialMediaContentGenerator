import Index from "layouts/Index.vue";
import Home from "pages/Home.vue";
import TwitterView from "pages/TwitterView.vue";

const routes = [
  {
    path: '/',
    component: Index,
    children: [
      { path: '', component: Home },
      { path: '/home' , name: 'home', component: Home},
      {path:  '/TwitterView', component: () => import('pages/TwitterView.vue')},
      { path: '/StableDiffusionUI', component: () => import('pages/StableDiffusionUI.vue')},
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
