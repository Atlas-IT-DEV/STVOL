import { createMemoryRouter, RouterProvider } from "react-router";
import MainPage from "./pages/mainPage/main_page";
import PageContainer from "./pages/page_container";
import ProfilePage from "./pages/profilePage/profile_page";

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
]);
function App() {
  return <RouterProvider router={router} />;
}

export default App;
