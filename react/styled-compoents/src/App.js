import styled, { ThemeProvider } from "styled-components";
import GlobalStyle from "./GlobalStyle";
import { useState } from "react";
import { dark, light } from "./theme";

const Wrapper = styled.section`
  background-color: ${props => props.theme.bgColor};
  color: ${props => props.theme.color};
  padding: 4em;
  text-align: center;
`;

const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
`;

function App() {
  const [isDark, setIsDark] = useState(true);
  const handleMode = () => setIsDark(!isDark);
  const theme = isDark ? dark : light;
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle/>
      <Wrapper>
        <Title>안녕하세요!</Title>
      </Wrapper>
      <button onClick={handleMode}>모드변경</button>
    </ThemeProvider>
  );
}
export default App;
