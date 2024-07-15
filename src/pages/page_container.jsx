import { VStack } from "@chakra-ui/react";

const PageContainer = ({ children }) => {
  return (
    <VStack minH={"100vh"} MaxWidth={"600px"} align={"center"}>
      <VStack width={"100%"}>{children}</VStack>
    </VStack>
  );
};

export default PageContainer;
