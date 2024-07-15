import { VStack, Stack, Text, Button } from "@chakra-ui/react";
import { useNavigate } from "react-router";

const InfoPage = () => {
  const navigate = useNavigate();
  return (
    <VStack width="100%" bgColor={"black"}>
      <Stack
        position={"absolute"}
        right={"10px"}
        top={"10px"}
        bgColor={"white"}
        width={"30px"}
        height={"30px"}
        borderRadius={"50%"}
        // display={"flex"}
        alignItems={"center"}
        justifyContent={"center"}
      >
        <Text textAlign={"center"}>✕</Text>
      </Stack>
      <Text color={"white"} fontSize={"50px"} textAlign={"center"}>
        STVOL
      </Text>
      <VStack
        color={"white"}
        width={"100%"}
        alignItems={"flex-start"}
        paddingLeft={10}
        paddingRight={10}
      >
        <Text fontSize={30}>О нас</Text>
        <Text marginTop={10}>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti a
          earum voluptate minus doloribus reprehenderit eligendi nulla sint non
          neque repudiandae ratione aliquid consequuntur, aliquam debitis
          incidunt, obcaecati ipsum modi.
        </Text>
        <Text>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti a
          earum voluptate minus doloribus reprehenderit eligendi nulla sint non
          neque repudiandae ratione aliquid consequuntur, aliquam debitis
          incidunt, obcaecati ipsum modi.
        </Text>
        <Text>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti a
          earum voluptate minus doloribus reprehenderit eligendi nulla sint non
          neque repudiandae ratione aliquid consequuntur, aliquam debitis
          incidunt, obcaecati ipsum modi.
        </Text>
        <Text>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti a
          earum voluptate minus doloribus reprehenderit eligendi nulla sint non
          neque repudiandae ratione aliquid consequuntur, aliquam debitis
          incidunt, obcaecati ipsum modi.
        </Text>
      </VStack>
      <VStack
        color={"white"}
        width={"100%"}
        alignItems={"flex-start"}
        paddingLeft={10}
        marginTop={10}
        marginBottom={10}
      >
        <Button width={"30%"} onClick={() => navigate("/profile")}>
          профиль
        </Button>
        <Button width={"30%"} onClick={() => navigate("/constructor")}>
          конструктор
        </Button>
        <Button width={"30%"} onClick={() => navigate("/")}>
          каталог
        </Button>
      </VStack>
    </VStack>
  );
};

export default InfoPage;
