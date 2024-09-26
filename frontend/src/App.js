// src/App.js

import React from 'react';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import theme from './theme';
import Header from './components/Header';
import PredictionForm from './components/PredictionForm';
import DataVisualization from './components/DataVisualization';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Header />
      <PredictionForm />
      <DataVisualization /> {/* Include the new component */}
    </ThemeProvider>
  );
}

export default App;
