html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>{%title%}</title>
                            {%favicon%}
                            {%css%}
                        </head>
                        <body>
                            <nav>
                              <a href="/"><i class="fas fa-home"></i> Home</a>
                            </nav>
                            {%app_entry%}
                            <footer>
                                {%config%}
                                {%scripts%}
                                {%renderer%}
                            </footer>
                        </body>
                    </html>'''