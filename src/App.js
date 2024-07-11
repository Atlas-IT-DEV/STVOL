import { createMemoryRouter, RouterProvider } from "react-router";
import MainPage from "./pages/main_page";
import PageContainer from "./pages/page_container";

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

      </PageContainer>
    ),
    path: "/1"
  },
  {}
]);
function App() {
  return <RouterProvider router={router} />;
}

export default App;
