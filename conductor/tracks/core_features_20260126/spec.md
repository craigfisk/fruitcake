# Core Features Specification - core_features_20260126

## Overview
This track focuses on implementing the foundational features of the Fruitcake App, enabling users to send digital fruitcake notes via email and track their journey on a map. This includes user authentication, the ability to select and customize fruitcake notes, integrate with email services for sending, and display the photo's path on a map.

## Functional Requirements

### User Authentication and Subscription Management
- **FR1.1:** The system SHALL allow users to register for a new account.
- **FR1.2:** The system SHALL allow registered users to log in and log out.
- **FR1.3:** The system SHALL manage user subscription statuses (e.g., free tier, premium tier).
- **FR1.4:** The system SHALL restrict photo sending functionality to authenticated and subscribed users.

### Fruitcake Photo Selection and Customization
- **FR2.1:** The system SHALL provide a gallery of high-quality fruitcake images for users to choose from.
- **FR2.2:** The system SHALL allow users to add personalized messages to selected fruitcake notes.
- **FR2.3:** The system SHALL allow users to preview the customized fruitcake photo before sending.

### Email Integration for Sending Fruitcake notes
- **FR3.1:** The system SHALL integrate with an email service to send customized fruitcake notes to specified recipient email addresses.
- **FR3.2:** The system SHALL allow users to specify multiple recipient email addresses for a single fruitcake photo.
- **FR3.3:** The sent email SHALL include the customized fruitcake photo and the personalized message.
- **FR3.4:** The sent email SHALL include a unique link for recipients to view the fruitcake photo's journey and optionally forward it.

### Real-time Tracking and Visualization on a Map
- **FR4.1:** The system SHALL record each instance of a fruitcake photo being sent and forwarded.
- **FR4.2:** The system SHALL generate a unique, shareable URL for each fruitcake photo's journey.
- **FR4.3:** The system SHALL display the journey of a fruitcake photo on a map (using Google Maps API) when a recipient accesses its unique URL.
- **FR4.4:** The map visualization SHALL show the sequence of locations where the fruitcake photo was sent/forwarded.

## Non-Functional Requirements

### Performance
- **NFR1.1:** The system SHALL display image galleries and map visualizations within 3 seconds under normal load.
- **NFR1.2:** Email sending SHALL be initiated within 5 seconds of a user confirming send.

### Security
- **NFR2.1:** User authentication credentials SHALL be securely stored and transmitted.
- **NFR2.2:** Access to user-specific data (e.g., sent notes, personalized messages) SHALL be restricted to the respective users.

### Usability
- **NFR3.1:** The user interface SHALL be intuitive and easy to navigate for all core functionalities.
- **NFR3.2:** Error messages SHALL be clear and provide actionable guidance to the user.

### Scalability
- **NFR4.1:** The system SHALL be capable of handling a growing number of users and fruitcake photo transactions without significant degradation in performance.

## Out of Scope
- Advanced image editing features beyond adding personalized messages.
- Social media sharing integrations (initial focus is email).
- Complex analytics dashboards for users (basic tracking map is sufficient).
