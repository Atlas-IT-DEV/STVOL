import { createMemoryRouter, RouterProvider } from "react-router";
import PageContainer from "./pages/page_container";
import ConstructorPage from "./pages/constructor_page/constructor_page";
import ProfilePage from "./pages/profile_page/profile_page";
import AboutPage from "./pages/about_page/about_page";
import CatalogPage from "./pages/catalog_page/catalog_page";
import LoyalityRulesPage from "./pages/rules_loyality_page/loyality_rules_page";
import ProductPage from "./pages/product_page/product_page";
import CartPage from "./pages/cart_page/cart_page";
import CheckoutPage from "./pages/checkout_page/checkout_page";
import { useEffect } from "react";
import { useStores } from "./store/store_context";

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
        <LoyalityRulesPage />
      </PageContainer>
    ),
    path: "/loyality_rules",
  },
  {
    element: (
      <PageContainer>
        <ProductPage />
      </PageContainer>
    ),
    path: "/product",
  },
  {
    element: (
      <PageContainer>
        <CartPage />
      </PageContainer>
    ),
    path: "/cart",
  },
  {
    element: (
      <PageContainer>
        <CheckoutPage />
      </PageContainer>
    ),
    path: "/checkout",
  },
]);
function App() {
  const { pageStore } = useStores();
  const tg = window.Telegram.WebApp;
  tg.enableClosingConfirmation();
  tg.expand();
  useEffect(() => {
    if (!tg.isExpanded) tg.expand();
  });
  tg.disableVerticalSwipes()
  tg.onEvent("viewportChanged", () => tg.expand());
  useEffect(() => {
    pageStore.signIn(
      tg?.initDataUnsafe?.user?.id ? tg?.initDataUnsafe?.user?.id : 11111,
      {
        name: `${tg?.initDataUnsafe?.user?.first_name} ${tg?.initDataUnsafe?.user?.last_name}`,
        telegram_id: tg?.initDataUnsafe?.user?.id
          ? tg?.initDataUnsafe?.user?.id
          : 11111,
        phone: tg?.initDataUnsafe?.user?.phone
          ? tg?.initDataUnsafe?.user?.phone
          : "880055535353",
        count_bonus: 0,
        referal: 0,
      }
    );
  }, []);
  return <RouterProvider router={router} />;
}

export default App;
