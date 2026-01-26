# Implementation Plan - core_features_20260126

This plan outlines the steps to implement the core features of the Fruitcake App, covering user authentication, fruitcake photo selection, email sending, and basic map tracking.

## Phase 1: User Authentication and Subscription Management

- [x] **Task: Set up backend for user authentication** [5e2c566]
    - [ ] Write Tests: For user registration, login, and logout endpoints.
    - [ ] Implement: User registration, login, and logout functionalities using FastAPI and Supabase.
- [x] **Task: Integrate subscription management with Supabase** [b71d6e7]
    - [ ] Write Tests: For managing user subscription statuses.
    - [ ] Implement: Logic to track and manage user subscriptions.
- [ ] **Task: Implement frontend authentication flow**
    - [ ] Write Tests: For user registration, login, and logout UI components and their interaction with the backend.
    - [ ] Implement: User registration, login, and logout UI using Vue.js.
- [ ] **Task: Conductor - User Manual Verification 'User Authentication and Subscription Management' (Protocol in workflow.md)**

## Phase 2: Fruitcake Photo Selection and Customization

- [ ] **Task: Create fruitcake image gallery backend**
    - [ ] Write Tests: For API endpoints to fetch fruitcake images.
    - [ ] Implement: Backend endpoints to serve a gallery of fruitcake images.
- [ ] **Task: Develop frontend fruitcake image gallery**
    - [ ] Write Tests: For UI components displaying the fruitcake image gallery.
    - [ ] Implement: Vue.js components to display and select fruitcake images.
- [ ] **Task: Implement photo customization features**
    - [ ] Write Tests: For backend and frontend logic to add personalized messages to photos.
    - [ ] Implement: Backend and frontend functionality for users to add personalized messages.
- [ ] **Task: Implement photo preview functionality**
    - [ ] Write Tests: For UI component to preview customized fruitcake photos.
    - [ ] Implement: Vue.js component to display a preview of the customized photo.
- [ ] **Task: Conductor - User Manual Verification 'Fruitcake Photo Selection and Customization' (Protocol in workflow.md)**

## Phase 3: Email Integration for Sending Fruitcake Photos

- [ ] **Task: Set up email sending service**
    - [ ] Write Tests: For email sending utility.
    - [ ] Implement: Backend integration with an email service to send emails.
- [ ] **Task: Implement backend endpoint for sending fruitcake photos**
    - [ ] Write Tests: For endpoint to handle sending customized fruitcake photos to recipients.
    - [ ] Implement: FastAPI endpoint to receive customized photo data and send emails.
- [ ] **Task: Develop frontend UI for sending photos**
    - [ ] Write Tests: For UI components to input recipient email addresses and trigger sending.
    - [ ] Implement: Vue.js components for recipient input and sending functionality.
- [ ] **Task: Conductor - User Manual Verification 'Email Integration for Sending Fruitcake Photos' (Protocol in workflow.md)**

## Phase 4: Real-time Tracking and Visualization on a Map

- [ ] **Task: Implement backend for tracking photo journeys**
    - [ ] Write Tests: For logic to record each send/forward event and generate unique tracking URLs.
    - [ ] Implement: FastAPI backend to record events and generate unique URLs.
- [ ] **Task: Integrate Google Maps API**
    - [ ] Write Tests: For frontend map display and interaction.
    - [ ] Implement: Frontend integration with Google Maps API to display the photo's journey.
- [ ] **Task: Develop map visualization UI**
    - [ ] Write Tests: For UI component to display the fruitcake photo's journey on a map.
    - [ ] Implement: Vue.js component to visualize the photo's path on Google Maps.
- [ ] **Task: Conductor - User Manual Verification 'Real-time Tracking and Visualization on a Map' (Protocol in workflow.md)**
