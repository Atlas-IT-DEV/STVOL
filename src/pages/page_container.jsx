import { VStack } from "@chakra-ui/react";

const PageContainer = ({ children }) => {
  return (
    <VStack maxWidth={"600px"} minH={"100vh"}>
      {children}
    </VStack>
  );
};

export default PageContainer;
