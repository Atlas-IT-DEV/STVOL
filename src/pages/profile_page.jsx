import {
  Stack,
  VStack,
  Text,
  Grid,
  GridItem,
  HStack,
  Image,
  Button,
} from "@chakra-ui/react";
import { useNavigate } from "react-router";

const ProfilePage = ({
  name = "Александр",
  numberPhone = "88005553535",
  scores = "352",
  count_adress = "2",
}) => {
  const navigate = useNavigate();
  return (
    <VStack bgColor={"black"} width={"100%"}>
      <Stack
        position={"absolute"}
        right={"10px"}
        top={"10px"}
        bgColor={"white"}
        width={"30px"}
        height={"30px"}
        borderRadius={"50%"}
        alignItems={"center"}
        justifyContent={"center"}
      >
        <Text>✕</Text>
      </Stack>
      <Text color={"white"} fontSize={"80px"}>
        STVOL
      </Text>
      <HStack justifyContent={"space-between"} width={"100%"}>
        <VStack
          color={"white"}
          fontSize={"20px"}
          textAlign={"center"}
          width={"100%"}
          height={"350px"}
          marginTop="10"
        >
          <Text fontSize={"30px"}>профиль</Text>
          <Text marginTop={5}>{name}</Text>
          <Text>{numberPhone}</Text>

          <Text marginTop={5}>Бонусы</Text>
          <Text
            color={"black"}
            background={"white"}
            width={"50%"}
            borderRadius={10}
          >
            {scores}
          </Text>

          <Text marginTop={5}>Адреса</Text>
          <Text
            color={"black"}
            background={"white"}
            width={"50%"}
            borderRadius={10}
          >
            {count_adress}
          </Text>
        </VStack>
        <VStack
          color={"white"}
          fontSize={"20px"}
          border={"1px solid white"}
          borderRadius={10}
          padding={5}
          width={"80%"}
          height={"350px"}
        >
          <Text fontSize={"30px"}>Заказы</Text>
          <Image height={250} width={"80%"} />
          <Button marginTop={5}>История заказов</Button>
        </VStack>
      </HStack>
      <HStack
        marginTop={5}
        justifyContent={"space-between"}
        width={"100%"}
        marginBottom={60}
      >
        <VStack width={"100%"} justifyContent={"space-between"} height={180}>
          <Button width={"80%"} fontSize={"26px"}>
            Редактировать
          </Button>
          <Button width={"80%"} fontSize={"26px"} height={"108px"}>
            Бонус за друга <br />
            15%
          </Button>
        </VStack>
        <VStack justifyContent={"space-between"} width={"100%"} height={180}>
          <Button
            width={"80%"}
            fontSize={"26px"}
            onClick={() => navigate("/about")}
          >
            что такое stvol?
          </Button>
          <Button
            width={"80%"}
            fontSize={"26px"}
            onClick={() => navigate("/constructor")}
          >
            конструктор
          </Button>
          <Button width={"80%"} fontSize={"26px"} onClick={() => navigate("/")}>
            каталог
          </Button>
        </VStack>
      </HStack>
    </VStack>
  );
};

export default ProfilePage;
