# Grazioso-Salvare-Database

## How do you write programs that are maintainable, readable, and adaptable?

I write maintainable, readable, and adaptable programs by separating different responsibilities into reusable components, using clear naming conventions, adding comments where they help explain the purpose of the code, and handling errors so that failures are easier to understand. One example of this approach was the CRUD Python module. Instead of placing MongoDB connection code and database commands directly inside the dashboard, I created an `AnimalShelter` class that contained reusable Create, Read, Update, and Delete methods.

This design made Grazioso Salvare easier because the dashboard could import the CRUD module and use its methods without rewriting the database logic. The dashboard widgets could focus on displaying information and responding to user input, while the CRUD module handled communication with MongoDB. This separation also makes the project easier to maintain because changes to the database connection or CRUD operations can be made in one location rather than throughout the application.

The CRUD module could also be reused in future applications that need access to the same animal shelter database. For example, it could support another dashboard, a reporting application, an administrative tool, or a different client-facing interface. The class could also be expanded with additional query methods if Grazioso Salvare needed more specialized ways to search or analyze the data.

## How do you approach a problem as a computer scientist?

I approach a problem by first identifying the client's requirements and breaking the larger problem into smaller tasks. For the Grazioso Salvare project, this included importing and organizing the animal shelter data, creating secure database access, developing reusable CRUD operations, and then connecting those operations to an interactive dashboard. I also needed to understand which characteristics Grazioso Salvare uses to identify rescue-animal candidates so that the database queries and dashboard filters could return useful results.

This project differed from many previous assignments because the individual parts had to work together as one client/server system. Instead of writing a program that only produced a specific output, I had to consider how the database, Python module, queries, authentication, and user interface would interact. Testing each part independently before integrating them helped identify problems and made the overall development process easier to manage.

For future database projects, I would continue to begin by studying the client's data requirements and identifying the entities, fields, relationships, and queries that the application will need. I would then design the database structure, test sample queries, create reusable data-access methods, and verify the results before connecting the database to the client-side application. I would also consider performance, indexing, security, validation, and future scalability as part of the design process.

## What do computer scientists do, and why does it matter?

Computer scientists use computing principles to solve problems, organize and process information, design software systems, and create tools that help people work more effectively. Their work involves more than writing code. It also includes analyzing requirements, designing systems, selecting appropriate technologies, testing solutions, improving performance, protecting data, and making software usable and maintainable.

The Grazioso Salvare project demonstrates why this work matters. The animal shelter data contains a large amount of information that would be difficult to review manually. By storing the information in MongoDB and creating a dashboard that can filter and display appropriate rescue-animal candidates, the application helps Grazioso Salvare find relevant animals more efficiently. Instead of manually searching through thousands of records, users can interact with the dashboard and quickly narrow the results based on the characteristics needed for different rescue situations.

A system like this can save an organization time, improve consistency, and help employees make better decisions using the information available to them. For Grazioso Salvare, that means spending less time searching through data and more time identifying and training animals that may eventually assist in search-and-rescue operations.
