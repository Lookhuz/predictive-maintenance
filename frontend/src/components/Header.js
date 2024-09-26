// src/components/Header.js

import React from 'react';
import { AppBar, Toolbar, Typography } from '@mui/material';

function Header() {
  return (
    <AppBar position="static" color="transparent" elevation={0}>
      <Toolbar>
        <Typography variant="h6" component="div">
          Predictive Maintenance
        </Typography>
      </Toolbar>
    </AppBar>
  );
}

export default Header;
