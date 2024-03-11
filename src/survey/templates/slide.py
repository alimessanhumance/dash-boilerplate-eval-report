from dash import html
import dash_bootstrap_components as dbc


def slide_layout():
    # Sample questions and options
    questions = [
        "What is your age group?",
        "How often do you exercise?",
        "What is your favorite color?",
    ]

    options = [
        ["Under 18", "18-30", "31-50", "Over 50"],
        ["Daily", "Weekly", "Monthly", "Rarely", "Never"],
        ["Red", "Blue", "Green", "Yellow", "Other"],
    ]

    # Create survey slides
    slides = []
    for i, question in enumerate(questions):
        options_radio = [
            dbc.RadioItems(
                options=[
                    {"label": option, "value": option}
                    for option in options[i]
                ],
                id=f"option-{i}",
                inline=True,
            )
        ]
        slide_content = html.Div(
            [
                html.H2(question),
                html.Div(options_radio),
            ],
            className="text-center",
        )
        slides.append(slide_content)

        return dbc.Container(
            [
                dbc.Row(
                    dbc.Col(
                        html.Div(
                            slides,
                            id="carousel-items",
                            className="carousel-inner",
                        ),
                        width={"size": 8, "offset": 2},
                        className="d-flex justify-content-center align-items-center",
                        style={"height": "90vh"},  # Fullscreen mode
                    )
                ),
                html.A(
                    dbc.Button("Previous", id="prev-slide", outline=True, color="primary"),
                    href="#",
                    className="carousel-control-prev",
                ),
                html.A(
                    dbc.Button("Next", id="next-slide", outline=True, color="primary"),
                    href="#",
                    className="carousel-control-next",
                ),
            ],
            fluid=True,
            className="p-5",
        )
