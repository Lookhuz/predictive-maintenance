// src/components/PredictionForm.js

import React, { useState } from 'react';
import axios from 'axios';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import {
  TextField,
  Button,
  Container,
  Typography,
  Box,
  CircularProgress,
} from '@mui/material';

function PredictionForm() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const formik = useFormik({
    initialValues: {
      temperature: '',
      vibration: '',
      pressure: '',
      operational_hours: '',
    },
    validationSchema: Yup.object({
      temperature: Yup.number()
        .required('Required')
        .min(0, 'Must be greater than or equal to 0')
        .max(200, 'Must be less than or equal to 200'),
      vibration: Yup.number()
        .required('Required')
        .min(0, 'Must be greater than or equal to 0')
        .max(5, 'Must be less than or equal to 5'),
      pressure: Yup.number()
        .required('Required')
        .min(0, 'Must be greater than or equal to 0')
        .max(100, 'Must be less than or equal to 100'),
      operational_hours: Yup.number()
        .required('Required')
        .min(0, 'Must be greater than or equal to 0'),
    }),
    onSubmit: async (values) => {
      setLoading(true);
      setError('');
      try {
        // Get token (hardcoded credentials for demo purposes)
        const tokenResponse = await axios.post(
          'http://localhost:8000/token',
          new URLSearchParams({
            username: 'user@example.com',
            password: 'password',
          }),
          {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
            },
          }
        );

        const token = tokenResponse.data.access_token;
        const headers = {
          Authorization: `Bearer ${token}`,
        };

        const response = await axios.post(
          'http://localhost:8000/predict',
          values,
          { headers }
        );
        alert(`Prediction: ${response.data.prediction}`);
      } catch (err) {
        console.error(err);
        setError('An error occurred.');
      } finally {
        setLoading(false);
      }
    },
  });

  return (
    <Container maxWidth="sm">
      <Box
        sx={{
          bgcolor: 'background.paper',
          p: 4,
          mt: 4,
          borderRadius: 2,
          boxShadow: 3,
        }}
      >
        <Typography variant="h5" gutterBottom>
          Enter Equipment Data
        </Typography>
        <form onSubmit={formik.handleSubmit}>
          <TextField
            fullWidth
            margin="normal"
            label="Temperature"
            name="temperature"
            type="number"
            value={formik.values.temperature}
            onChange={formik.handleChange}
            error={
              formik.touched.temperature && Boolean(formik.errors.temperature)
            }
            helperText={formik.touched.temperature && formik.errors.temperature}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Vibration"
            name="vibration"
            type="number"
            value={formik.values.vibration}
            onChange={formik.handleChange}
            error={
              formik.touched.vibration && Boolean(formik.errors.vibration)
            }
            helperText={formik.touched.vibration && formik.errors.vibration}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Pressure"
            name="pressure"
            type="number"
            value={formik.values.pressure}
            onChange={formik.handleChange}
            error={formik.touched.pressure && Boolean(formik.errors.pressure)}
            helperText={formik.touched.pressure && formik.errors.pressure}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Operational Hours"
            name="operational_hours"
            type="number"
            value={formik.values.operational_hours}
            onChange={formik.handleChange}
            error={
              formik.touched.operational_hours &&
              Boolean(formik.errors.operational_hours)
            }
            helperText={
              formik.touched.operational_hours &&
              formik.errors.operational_hours
            }
          />
          <Button
            color="primary"
            variant="contained"
            type="submit"
            fullWidth
            disabled={loading}
            sx={{ mt: 3 }}
          >
            {loading ? <CircularProgress size={24} /> : 'Predict'}
          </Button>
          {error && (
            <Typography color="error" sx={{ mt: 2 }}>
              {error}
            </Typography>
          )}
        </form>
      </Box>
    </Container>
  );
}

export default PredictionForm;
