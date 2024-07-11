import { VStack, Heading } from "@chakra-ui/react";
import "./main_page.css";

const MainPage = () => {
  return (
    <VStack width={"100%"}>
      <Heading>
        ЭТО ГЛАВНАЯ СТРАНИЦА, не вздумай ставить страницы без page_container.jsx
        в роутер. Padding общие для всей страницы тоже ставь в page_container
      </Heading>
      <p id="alertion">иначе дам пизды</p>
    </VStack>
  );
};
export default MainPage;
