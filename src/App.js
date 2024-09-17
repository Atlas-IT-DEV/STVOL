import { createMemoryRouter, RouterProvider } from "react-router";
import PageContainer from "./pages/page_container";
import ConstructorPage from "./pages/constructor_page/constructor_page";

const router = createMemoryRouter([
  {
    element: (
      <PageContainer>
        <ConstructorPage />
      </PageContainer>
    ),
    path: "/",
  },
]);
function App() {
  return <RouterProvider router={router} />;
}

export default App;
