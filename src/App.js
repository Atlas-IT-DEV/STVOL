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
]);
function App() {
  return <RouterProvider router={router} />;
}

export default App;
