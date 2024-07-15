import { createMemoryRouter, RouterProvider } from "react-router";
import MainPage from "./pages/main_page";
import ProfilePage from "./pages/profile_page";
import PageContainer from "./pages/page_container";
import InfoPage from "./pages/info_page";
import ConstructorPage from "./pages/constructor_page";


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
        <InfoPage/>
      </PageContainer>
    ),
    path: "/about",
  },
  {
    element: (
      <PageContainer>
        <ConstructorPage/>
      </PageContainer>
    ),
    path: "/constructor",
  },
]);
function App() {
  return <RouterProvider router={router} />;
}

export default App;
