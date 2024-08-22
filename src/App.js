import { createMemoryRouter, RouterProvider } from "react-router";
import MainPage from "./pages/mainPage/main_page";
import PageContainer from "./pages/page_container";
import ProfilePage from "./pages/profilePage/profile_page";
import CatalogPage from "./pages/catalogPage/catalog_page";
import InfoPage from "./pages/infoPage/info_page";

const router = createMemoryRouter([
  {
    element: (
      <PageContainer>
        <MainPage />
      </PageContainer>
    ),
    path: "/",
  },

  {
    element: (
      <PageContainer>
        <ProfilePage />
      </PageContainer>
    ),
    path: "/profile",
  },
  {
    element: (
      <PageContainer>
        <CatalogPage />
      </PageContainer>
    ),
    path: "/catalog",
  },
  {
    element: (
      <PageContainer>
        <InfoPage />
      </PageContainer>
    ),
    path: "/info",
  },
]);
function App() {
  return <RouterProvider router={router} />;
}

export default App;
