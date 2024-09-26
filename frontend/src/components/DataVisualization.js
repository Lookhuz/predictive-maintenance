// src/components/DataVisualization.js

import React from 'react';
import {
  Container,
  Typography,
  Box,
  Card,
  CardMedia,
  CardContent,
} from '@mui/material';

const images = [
  {
    src: '/images/correlation_matrix.png',
    title: 'Correlation Matrix',
    description:
      'This heatmap shows the correlation between different variables in the dataset. A higher absolute value indicates a stronger relationship.',
  },
  {
    src: '/images/temperature_distribution.png',
    title: 'Temperature Distribution',
    description:
      'Histogram showing the distribution of temperature readings across the dataset.',
  },
  {
    src: '/images/vibration_distribution.png',
    title: 'Vibration Distribution',
    description:
      'Histogram showing the distribution of vibration readings across the dataset.',
  },
  {
    src: '/images/pressure_distribution.png',
    title: 'Pressure Distribution',
    description:
      'Histogram showing the distribution of pressure readings across the dataset.',
  },
  {
    src: '/images/operational_hours_distribution.png',
    title: 'Operational Hours Distribution',
    description:
      'Histogram showing the distribution of operational hours across the dataset.',
  },
  {
    src: '/images/temp_pressure_interaction_distribution.png',
    title: 'Temperature-Pressure Interaction Distribution',
    description:
      'Histogram showing the distribution of the interaction term between temperature and pressure.',
  },
  {
    src: '/images/vibration_squared_distribution.png',
    title: 'Vibration Squared Distribution',
    description:
      'Histogram showing the distribution of the squared vibration values.',
  },
  {
    src: '/images/failure_distribution.png',
    title: 'Failure Distribution',
    description:
      'Histogram showing the distribution of failure occurrences in the dataset.',
  },
];

function DataVisualization() {
  return (
    <Container maxWidth="md" sx={{ mt: 10 }}>
      <Typography variant="h4" gutterBottom>
        Data Visualization
      </Typography>
      {images.map((image, index) => (
        <Box key={index} sx={{ mb: 4 }}>
          <Card sx={{ backgroundColor: 'background.paper' }}>
            <CardMedia
              component="img"
              image={image.src}
              alt={image.title}
            />
            <CardContent>
              <Typography variant="h5" gutterBottom>
                {image.title}
              </Typography>
              <Typography variant="body1">{image.description}</Typography>
            </CardContent>
          </Card>
        </Box>
      ))}
    </Container>
  );
}

export default DataVisualization;
