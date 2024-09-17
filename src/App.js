import { createMemoryRouter, RouterProvider } from "react-router";
import PageContainer from "./pages/page_container";
import ConstructorPage from "./pages/constructor_page/constructor_page";
import ProfilePage from "./pages/profile_page/profile_page";
import AboutPage from "./pages/about_page/about_page";

const router = createMemoryRouter([
  {
    element: (
      <PageContainer>
        <ConstructorPage />
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
        <AboutPage />
      </PageContainer>
    ),
    path: "/about",
  },
]);
function App() {
  return <RouterProvider router={router} />;
}

export default App;
