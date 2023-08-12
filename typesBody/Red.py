def getBodyRED(x, y):
    body = f"""{{
  "expression": {{
    "result": "0",
    "values": {{
      "0": {{
        "functionInvocationValue": {{
          "arguments": {{
            "dictionary": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "collection": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "collection": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "collection": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "collection1": {{
                                      "valueReference": "1"
                                    }},
                                    "collection2": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "images": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "list": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "list": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "start": {{
                                                              "functionInvocationValue": {{
                                                                "arguments": {{
                                                                  "date": {{
                                                                    "functionInvocationValue": {{
                                                                      "arguments": {{
                                                                        "image": {{
                                                                          "functionInvocationValue": {{
                                                                            "arguments": {{
                                                                              "collection": {{
                                                                                "valueReference": "1"
                                                                              }}
                                                                            }},
                                                                            "functionName": "Collection.first"
                                                                          }}
                                                                        }}
                                                                      }},
                                                                      "functionName": "Image.date"
                                                                    }}
                                                                  }},
                                                                  "unit": {{
                                                                    "valueReference": "67"
                                                                  }}
                                                                }},
                                                                "functionName": "Date.get"
                                                              }}
                                                            }},
                                                            "end": {{
                                                              "functionInvocationValue": {{
                                                                "arguments": {{
                                                                  "date": {{
                                                                    "functionInvocationValue": {{
                                                                      "arguments": {{
                                                                        "image": {{
                                                                          "functionInvocationValue": {{
                                                                            "arguments": {{
                                                                              "collection": {{
                                                                                "functionInvocationValue": {{
                                                                                  "arguments": {{
                                                                                    "collection": {{
                                                                                      "valueReference": "1"
                                                                                    }},
                                                                                    "key": {{
                                                                                      "valueReference": "38"
                                                                                    }},
                                                                                    "ascending": {{
                                                                                      "constantValue": false
                                                                                    }}
                                                                                  }},
                                                                                  "functionName": "Collection.limit"
                                                                                }}
                                                                              }}
                                                                            }},
                                                                            "functionName": "Collection.first"
                                                                          }}
                                                                        }}
                                                                      }},
                                                                      "functionName": "Image.date"
                                                                    }}
                                                                  }},
                                                                  "unit": {{
                                                                    "valueReference": "67"
                                                                  }}
                                                                }},
                                                                "functionName": "Date.get"
                                                              }}
                                                            }},
                                                            "step": {{
                                                              "constantValue": 0.1
                                                            }}
                                                          }},
                                                          "functionName": "List.sequence"
                                                        }}
                                                      }},
                                                      "baseAlgorithm": {{
                                                        "functionDefinitionValue": {{
                                                          "argumentNames": [
                                                            "_MAPPING_VAR_0_0"
                                                          ],
                                                          "body": "68"
                                                        }}
                                                      }}
                                                    }},
                                                    "functionName": "List.map"
                                                  }}
                                                }},
                                                "baseAlgorithm": {{
                                                  "functionDefinitionValue": {{
                                                    "argumentNames": [
                                                      "_MAPPING_VAR_0_0"
                                                    ],
                                                    "body": "71"
                                                  }}
                                                }}
                                              }},
                                              "functionName": "List.map"
                                            }}
                                          }}
                                        }},
                                        "functionName": "ImageCollection.fromImages"
                                      }}
                                    }}
                                  }},
                                  "functionName": "ImageCollection.merge"
                                }}
                              }},
                              "key": {{
                                "valueReference": "38"
                              }}
                            }},
                            "functionName": "Collection.limit"
                          }}
                        }},
                        "baseAlgorithm": {{
                          "functionDefinitionValue": {{
                            "argumentNames": [
                              "_MAPPING_VAR_4_0"
                            ],
                            "body": "72"
                          }}
                        }}
                      }},
                      "functionName": "Collection.map"
                    }}
                  }},
                  "reducer": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "tupleSize": {{
                          "valueReference": "92"
                        }},
                        "numOptional": {{
                          "valueReference": "92"
                        }}
                      }},
                      "functionName": "Reducer.toList"
                    }}
                  }},
                  "selectors": {{
                    "arrayValue": {{
                      "values": [
                        {{
                          "valueReference": "91"
                        }},
                        {{
                          "valueReference": "73"
                        }},
                        {{
                          "constantValue": "h0"
                        }},
                        {{
                          "constantValue": "h1"
                        }},
                        {{
                          "constantValue": "h2"
                        }},
                        {{
                          "constantValue": "h3"
                        }},
                        {{
                          "constantValue": "h4"
                        }},
                        {{
                          "constantValue": "h5"
                        }},
                        {{
                          "valueReference": "79"
                        }}
                      ]
                    }}
                  }}
                }},
                "functionName": "Collection.reduceColumns"
              }}
            }},
            "key": {{
              "constantValue": "list"
            }}
          }},
          "functionName": "Dictionary.get"
        }}
      }},
      "1": {{
        "functionInvocationValue": {{
          "arguments": {{
            "collection": {{
              "valueReference": "2"
            }},
            "key": {{
              "valueReference": "38"
            }}
          }},
          "functionName": "Collection.limit"
        }}
      }},
      "2": {{
        "functionInvocationValue": {{
          "arguments": {{
            "collection": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "collection": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "collection": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "collection1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "collection1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "collection1": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "collection": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "collection": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "collection": {{
                                                              "functionInvocationValue": {{
                                                                "arguments": {{
                                                                  "id": {{
                                                                    "constantValue": "LANDSAT/LC08/C02/T1_L2"
                                                                  }}
                                                                }},
                                                                "functionName": "ImageCollection.load"
                                                              }}
                                                            }},
                                                            "filter": {{
                                                              "valueReference": "3"
                                                            }}
                                                          }},
                                                          "functionName": "Collection.filter"
                                                        }}
                                                      }},
                                                      "filter": {{
                                                        "valueReference": "4"
                                                      }}
                                                    }},
                                                    "functionName": "Collection.filter"
                                                  }}
                                                }},
                                                "baseAlgorithm": {{
                                                  "functionDefinitionValue": {{
                                                    "argumentNames": [
                                                      "_MAPPING_VAR_0_0"
                                                    ],
                                                    "body": "6"
                                                  }}
                                                }}
                                              }},
                                              "functionName": "Collection.map"
                                            }}
                                          }},
                                          "collection2": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "collection": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "collection": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "collection": {{
                                                              "functionInvocationValue": {{
                                                                "arguments": {{
                                                                  "id": {{
                                                                    "constantValue": "LANDSAT/LE07/C02/T1_L2"
                                                                  }}
                                                                }},
                                                                "functionName": "ImageCollection.load"
                                                              }}
                                                            }},
                                                            "filter": {{
                                                              "valueReference": "3"
                                                            }}
                                                          }},
                                                          "functionName": "Collection.filter"
                                                        }}
                                                      }},
                                                      "filter": {{
                                                        "valueReference": "4"
                                                      }}
                                                    }},
                                                    "functionName": "Collection.filter"
                                                  }}
                                                }},
                                                "baseAlgorithm": {{
                                                  "valueReference": "33"
                                                }}
                                              }},
                                              "functionName": "Collection.map"
                                            }}
                                          }}
                                        }},
                                        "functionName": "ImageCollection.merge"
                                      }}
                                    }},
                                    "collection2": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "collection": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "collection": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "collection": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "id": {{
                                                              "constantValue": "LANDSAT/LT05/C02/T1_L2"
                                                            }}
                                                          }},
                                                          "functionName": "ImageCollection.load"
                                                        }}
                                                      }},
                                                      "filter": {{
                                                        "valueReference": "3"
                                                      }}
                                                    }},
                                                    "functionName": "Collection.filter"
                                                  }}
                                                }},
                                                "filter": {{
                                                  "valueReference": "4"
                                                }}
                                              }},
                                              "functionName": "Collection.filter"
                                            }}
                                          }},
                                          "baseAlgorithm": {{
                                            "valueReference": "33"
                                          }}
                                        }},
                                        "functionName": "Collection.map"
                                      }}
                                    }}
                                  }},
                                  "functionName": "ImageCollection.merge"
                                }}
                              }},
                              "collection2": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "collection": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "collection": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "collection": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "id": {{
                                                        "constantValue": "LANDSAT/LT04/C02/T1_L2"
                                                      }}
                                                    }},
                                                    "functionName": "ImageCollection.load"
                                                  }}
                                                }},
                                                "filter": {{
                                                  "valueReference": "3"
                                                }}
                                              }},
                                              "functionName": "Collection.filter"
                                            }}
                                          }},
                                          "filter": {{
                                            "valueReference": "4"
                                          }}
                                        }},
                                        "functionName": "Collection.filter"
                                      }}
                                    }},
                                    "baseAlgorithm": {{
                                      "valueReference": "33"
                                    }}
                                  }},
                                  "functionName": "Collection.map"
                                }}
                              }}
                            }},
                            "functionName": "ImageCollection.merge"
                          }}
                        }},
                        "filter": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "rightField": {{
                                "valueReference": "38"
                              }},
                              "leftValue": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "start": {{
                                      "constantValue": "2000-01-01"
                                    }},
                                    "end": {{
                                      "constantValue": "2023-01-01"
                                    }}
                                  }},
                                  "functionName": "DateRange"
                                }}
                              }}
                            }},
                            "functionName": "Filter.dateRangeContains"
                          }}
                        }}
                      }},
                      "functionName": "Collection.filter"
                    }}
                  }},
                  "baseAlgorithm": {{
                    "functionDefinitionValue": {{
                      "argumentNames": [
                        "_MAPPING_VAR_0_0"
                      ],
                      "body": "39"
                    }}
                  }}
                }},
                "functionName": "Collection.map"
              }}
            }},
            "baseAlgorithm": {{
              "functionDefinitionValue": {{
                "argumentNames": [
                  "_MAPPING_VAR_0_0"
                ],
                "body": "40"
              }}
            }}
          }},
          "functionName": "Collection.map"
        }}
      }},
      "3": {{
        "constantValue": "WRS_ROW < 122"
      }},
      "4": {{
        "functionInvocationValue": {{
          "arguments": {{
            "leftField": {{
              "constantValue": ".all"
            }},
            "rightValue": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "geometry": {{
                    "valueReference": "5"
                  }}
                }},
                "functionName": "Feature"
              }}
            }}
          }},
          "functionName": "Filter.intersects"
        }}
      }},
      "5": {{
        "functionInvocationValue": {{
          "arguments": {{
            "coordinates": {{
              "constantValue": [
                {x},
                {y}
              ]
            }}
          }},
          "functionName": "GeometryConstructors.Point"
        }}
      }},
      "6": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "dstImg": {{
                    "argumentReference": "_MAPPING_VAR_0_0"
                  }},
                  "srcImg": {{
                    "valueReference": "7"
                  }}
                }},
                "functionName": "Image.addBands"
              }}
            }},
            "mask": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "image1": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image1": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "image": {{
                                            "valueReference": "24"
                                          }},
                                          "from": {{
                                            "constantValue": [
                                              21824,
                                              21888
                                            ]
                                          }},
                                          "to": {{
                                            "valueReference": "25"
                                          }},
                                          "defaultValue": {{
                                            "constantValue": 0
                                          }}
                                        }},
                                        "functionName": "Image.remap"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "26"
                                    }}
                                  }},
                                  "functionName": "Image.and"
                                }}
                              }},
                              "image2": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "image": {{
                                            "valueReference": "28"
                                          }},
                                          "reducer": {{
                                            "valueReference": "30"
                                          }}
                                        }},
                                        "functionName": "Image.reduce"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "27"
                                    }}
                                  }},
                                  "functionName": "Image.gt"
                                }}
                              }}
                            }},
                            "functionName": "Image.and"
                          }}
                        }},
                        "image2": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image": {{
                                      "valueReference": "28"
                                    }},
                                    "reducer": {{
                                      "valueReference": "31"
                                    }}
                                  }},
                                  "functionName": "Image.reduce"
                                }}
                              }},
                              "image2": {{
                                "valueReference": "32"
                              }}
                            }},
                            "functionName": "Image.lt"
                          }}
                        }}
                      }},
                      "functionName": "Image.and"
                    }}
                  }},
                  "image2": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "input": {{
                                "argumentReference": "_MAPPING_VAR_0_0"
                              }},
                              "bandSelectors": {{
                                "constantValue": [
                                  "SR_QA_AEROSOL"
                                ]
                              }}
                            }},
                            "functionName": "Image.select"
                          }}
                        }},
                        "from": {{
                          "constantValue": [
                            2,
                            4,
                            32,
                            66,
                            68,
                            96,
                            100,
                            130,
                            132,
                            160,
                            164
                          ]
                        }},
                        "to": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "value": {{
                                "constantValue": 1
                              }},
                              "count": {{
                                "constantValue": 11
                              }}
                            }},
                            "functionName": "List.repeat"
                          }}
                        }},
                        "defaultValue": {{
                          "constantValue": 0
                        }}
                      }},
                      "functionName": "Image.remap"
                    }}
                  }}
                }},
                "functionName": "Image.and"
              }}
            }}
          }},
          "functionName": "Image.updateMask"
        }}
      }},
      "7": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "input": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "dstImg": {{
                          "valueReference": "8"
                        }},
                        "srcImg": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "argumentReference": "_MAPPING_VAR_0_0"
                                          }},
                                          "bandSelectors": {{
                                            "arrayValue": {{
                                              "values": [
                                                {{
                                                  "valueReference": "9"
                                                }}
                                              ]
                                            }}
                                          }}
                                        }},
                                        "functionName": "Image.select"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "10"
                                    }}
                                  }},
                                  "functionName": "Image.multiply"
                                }}
                              }},
                              "image2": {{
                                "valueReference": "11"
                              }}
                            }},
                            "functionName": "Image.add"
                          }}
                        }},
                        "names": {{
                          "constantValue": null
                        }},
                        "overwrite": {{
                          "constantValue": true
                        }}
                      }},
                      "functionName": "Image.addBands"
                    }}
                  }},
                  "bandSelectors": {{
                    "arrayValue": {{
                      "values": [
                        {{
                          "valueReference": "12"
                        }},
                        {{
                          "valueReference": "13"
                        }},
                        {{
                          "valueReference": "14"
                        }},
                        {{
                          "valueReference": "15"
                        }},
                        {{
                          "constantValue": "SR_B6"
                        }},
                        {{
                          "valueReference": "16"
                        }},
                        {{
                          "valueReference": "9"
                        }}
                      ]
                    }}
                  }}
                }},
                "functionName": "Image.select"
              }}
            }},
            "names": {{
              "valueReference": "17"
            }}
          }},
          "functionName": "Image.rename"
        }}
      }},
      "8": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image1": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "image1": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "input": {{
                          "argumentReference": "_MAPPING_VAR_0_0"
                        }},
                        "bandSelectors": {{
                          "constantValue": [
                            "SR_B."
                          ]
                        }}
                      }},
                      "functionName": "Image.select"
                    }}
                  }},
                  "image2": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "value": {{
                          "constantValue": 0.0000275
                        }}
                      }},
                      "functionName": "Image.constant"
                    }}
                  }}
                }},
                "functionName": "Image.multiply"
              }}
            }},
            "image2": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "value": {{
                    "constantValue": -0.2
                  }}
                }},
                "functionName": "Image.constant"
              }}
            }}
          }},
          "functionName": "Image.add"
        }}
      }},
      "9": {{
        "constantValue": "ST_B10"
      }},
      "10": {{
        "functionInvocationValue": {{
          "arguments": {{
            "value": {{
              "constantValue": 0.00341802
            }}
          }},
          "functionName": "Image.constant"
        }}
      }},
      "11": {{
        "functionInvocationValue": {{
          "arguments": {{
            "value": {{
              "constantValue": 149
            }}
          }},
          "functionName": "Image.constant"
        }}
      }},
      "12": {{
        "constantValue": "SR_B2"
      }},
      "13": {{
        "constantValue": "SR_B3"
      }},
      "14": {{
        "constantValue": "SR_B4"
      }},
      "15": {{
        "constantValue": "SR_B5"
      }},
      "16": {{
        "constantValue": "SR_B7"
      }},
      "17": {{
        "arrayValue": {{
          "values": [
            {{
              "valueReference": "18"
            }},
            {{
              "valueReference": "19"
            }},
            {{
              "valueReference": "20"
            }},
            {{
              "valueReference": "21"
            }},
            {{
              "valueReference": "22"
            }},
            {{
              "valueReference": "23"
            }},
            {{
              "constantValue": "TEMP"
            }}
          ]
        }}
      }},
      "18": {{
        "constantValue": "BLUE"
      }},
      "19": {{
        "constantValue": "GREEN"
      }},
      "20": {{
        "constantValue": "RED"
      }},
      "21": {{
        "constantValue": "NIR"
      }},
      "22": {{
        "constantValue": "SWIR1"
      }},
      "23": {{
        "constantValue": "SWIR2"
      }},
      "24": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "constantValue": [
                "QA_PIXEL"
              ]
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "25": {{
        "functionInvocationValue": {{
          "arguments": {{
            "value": {{
              "constantValue": 1
            }},
            "count": {{
              "constantValue": 2
            }}
          }},
          "functionName": "List.repeat"
        }}
      }},
      "26": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image1": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "input": {{
                    "argumentReference": "_MAPPING_VAR_0_0"
                  }},
                  "bandSelectors": {{
                    "constantValue": [
                      "QA_RADSAT"
                    ]
                  }}
                }},
                "functionName": "Image.select"
              }}
            }},
            "image2": {{
              "valueReference": "27"
            }}
          }},
          "functionName": "Image.eq"
        }}
      }},
      "27": {{
        "functionInvocationValue": {{
          "arguments": {{
            "value": {{
              "constantValue": 0
            }}
          }},
          "functionName": "Image.constant"
        }}
      }},
      "28": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "valueReference": "7"
            }},
            "bandSelectors": {{
              "valueReference": "29"
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "29": {{
        "arrayValue": {{
          "values": [
            {{
              "valueReference": "18"
            }},
            {{
              "valueReference": "19"
            }},
            {{
              "valueReference": "20"
            }},
            {{
              "valueReference": "21"
            }},
            {{
              "valueReference": "22"
            }},
            {{
              "valueReference": "23"
            }}
          ]
        }}
      }},
      "30": {{
        "functionInvocationValue": {{
          "arguments": {{}},
          "functionName": "Reducer.min"
        }}
      }},
      "31": {{
        "functionInvocationValue": {{
          "arguments": {{}},
          "functionName": "Reducer.max"
        }}
      }},
      "32": {{
        "functionInvocationValue": {{
          "arguments": {{
            "value": {{
              "constantValue": 1
            }}
          }},
          "functionName": "Image.constant"
        }}
      }},
      "33": {{
        "functionDefinitionValue": {{
          "argumentNames": [
            "_MAPPING_VAR_0_0"
          ],
          "body": "34"
        }}
      }},
      "34": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "dstImg": {{
                    "argumentReference": "_MAPPING_VAR_0_0"
                  }},
                  "srcImg": {{
                    "valueReference": "35"
                  }}
                }},
                "functionName": "Image.addBands"
              }}
            }},
            "mask": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "image1": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image1": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "image": {{
                                            "valueReference": "24"
                                          }},
                                          "from": {{
                                            "constantValue": [
                                              5440,
                                              5504
                                            ]
                                          }},
                                          "to": {{
                                            "valueReference": "25"
                                          }},
                                          "defaultValue": {{
                                            "constantValue": 0
                                          }}
                                        }},
                                        "functionName": "Image.remap"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "26"
                                    }}
                                  }},
                                  "functionName": "Image.and"
                                }}
                              }},
                              "image2": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "image": {{
                                            "valueReference": "37"
                                          }},
                                          "reducer": {{
                                            "valueReference": "30"
                                          }}
                                        }},
                                        "functionName": "Image.reduce"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "27"
                                    }}
                                  }},
                                  "functionName": "Image.gt"
                                }}
                              }}
                            }},
                            "functionName": "Image.and"
                          }}
                        }},
                        "image2": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image": {{
                                      "valueReference": "37"
                                    }},
                                    "reducer": {{
                                      "valueReference": "31"
                                    }}
                                  }},
                                  "functionName": "Image.reduce"
                                }}
                              }},
                              "image2": {{
                                "valueReference": "32"
                              }}
                            }},
                            "functionName": "Image.lt"
                          }}
                        }}
                      }},
                      "functionName": "Image.and"
                    }}
                  }},
                  "image2": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image1": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "input": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "argumentReference": "_MAPPING_VAR_0_0"
                                    }},
                                    "bandSelectors": {{
                                      "constantValue": [
                                        "SR_ATMOS_OPACITY"
                                      ]
                                    }}
                                  }},
                                  "functionName": "Image.select"
                                }}
                              }},
                              "value": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "value": {{
                                      "constantValue": -1
                                    }}
                                  }},
                                  "functionName": "Image.constant"
                                }}
                              }}
                            }},
                            "functionName": "Image.unmask"
                          }}
                        }},
                        "image2": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "value": {{
                                "constantValue": 300
                              }}
                            }},
                            "functionName": "Image.constant"
                          }}
                        }}
                      }},
                      "functionName": "Image.lt"
                    }}
                  }}
                }},
                "functionName": "Image.and"
              }}
            }}
          }},
          "functionName": "Image.updateMask"
        }}
      }},
      "35": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "input": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "dstImg": {{
                          "valueReference": "8"
                        }},
                        "srcImg": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "argumentReference": "_MAPPING_VAR_0_0"
                                          }},
                                          "bandSelectors": {{
                                            "arrayValue": {{
                                              "values": [
                                                {{
                                                  "valueReference": "36"
                                                }}
                                              ]
                                            }}
                                          }}
                                        }},
                                        "functionName": "Image.select"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "10"
                                    }}
                                  }},
                                  "functionName": "Image.multiply"
                                }}
                              }},
                              "image2": {{
                                "valueReference": "11"
                              }}
                            }},
                            "functionName": "Image.add"
                          }}
                        }},
                        "names": {{
                          "constantValue": null
                        }},
                        "overwrite": {{
                          "constantValue": true
                        }}
                      }},
                      "functionName": "Image.addBands"
                    }}
                  }},
                  "bandSelectors": {{
                    "arrayValue": {{
                      "values": [
                        {{
                          "constantValue": "SR_B1"
                        }},
                        {{
                          "valueReference": "12"
                        }},
                        {{
                          "valueReference": "13"
                        }},
                        {{
                          "valueReference": "14"
                        }},
                        {{
                          "valueReference": "15"
                        }},
                        {{
                          "valueReference": "16"
                        }},
                        {{
                          "valueReference": "36"
                        }}
                      ]
                    }}
                  }}
                }},
                "functionName": "Image.select"
              }}
            }},
            "names": {{
              "valueReference": "17"
            }}
          }},
          "functionName": "Image.rename"
        }}
      }},
      "36": {{
        "constantValue": "ST_B6"
      }},
      "37": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "valueReference": "35"
            }},
            "bandSelectors": {{
              "valueReference": "29"
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "38": {{
        "constantValue": "system:time_start"
      }},
      "39": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "valueReference": "29"
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "40": {{
        "functionInvocationValue": {{
          "arguments": {{
            "dstImg": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "srcImg": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "dstImg": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "dstImg": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "dstImg": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "dstImg": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "dstImg": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "input": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "input": {{
                                                        "argumentReference": "_MAPPING_VAR_0_0"
                                                      }},
                                                      "bandNames": {{
                                                        "arrayValue": {{
                                                          "values": [
                                                            {{
                                                              "valueReference": "21"
                                                            }},
                                                            {{
                                                              "valueReference": "20"
                                                            }}
                                                          ]
                                                        }}
                                                      }}
                                                    }},
                                                    "functionName": "Image.normalizedDifference"
                                                  }}
                                                }},
                                                "names": {{
                                                  "constantValue": [
                                                    "NDVI"
                                                  ]
                                                }}
                                              }},
                                              "functionName": "Image.rename"
                                            }}
                                          }},
                                          "srcImg": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "input": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "input": {{
                                                        "argumentReference": "_MAPPING_VAR_0_0"
                                                      }},
                                                      "bandNames": {{
                                                        "arrayValue": {{
                                                          "values": [
                                                            {{
                                                              "valueReference": "21"
                                                            }},
                                                            {{
                                                              "valueReference": "23"
                                                            }}
                                                          ]
                                                        }}
                                                      }}
                                                    }},
                                                    "functionName": "Image.normalizedDifference"
                                                  }}
                                                }},
                                                "names": {{
                                                  "constantValue": [
                                                    "NBR"
                                                  ]
                                                }}
                                              }},
                                              "functionName": "Image.rename"
                                            }}
                                          }}
                                        }},
                                        "functionName": "Image.addBands"
                                      }}
                                    }},
                                    "srcImg": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "DEFAULT_EXPRESSION_IMAGE": {{
                                                  "argumentReference": "_MAPPING_VAR_0_0"
                                                }},
                                                "B4": {{
                                                  "valueReference": "41"
                                                }},
                                                "B3": {{
                                                  "valueReference": "42"
                                                }},
                                                "B1": {{
                                                  "valueReference": "44"
                                                }}
                                              }},
                                              "functionReference": "45"
                                            }}
                                          }},
                                          "names": {{
                                            "constantValue": [
                                              "EVI"
                                            ]
                                          }}
                                        }},
                                        "functionName": "Image.rename"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Image.addBands"
                                }}
                              }},
                              "srcImg": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "DEFAULT_EXPRESSION_IMAGE": {{
                                            "argumentReference": "_MAPPING_VAR_0_0"
                                          }},
                                          "B4": {{
                                            "valueReference": "41"
                                          }},
                                          "B3": {{
                                            "valueReference": "42"
                                          }}
                                        }},
                                        "functionReference": "51"
                                      }}
                                    }},
                                    "names": {{
                                      "constantValue": [
                                        "EVI2"
                                      ]
                                    }}
                                  }},
                                  "functionName": "Image.rename"
                                }}
                              }}
                            }},
                            "functionName": "Image.addBands"
                          }}
                        }},
                        "srcImg": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "dstImg": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "dstImg": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "DEFAULT_EXPRESSION_IMAGE": {{
                                                  "argumentReference": "_MAPPING_VAR_0_0"
                                                }},
                                                "L1": {{
                                                  "valueReference": "44"
                                                }},
                                                "B1": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.2043
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L2": {{
                                                  "valueReference": "52"
                                                }},
                                                "B2": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.4158
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L3": {{
                                                  "valueReference": "42"
                                                }},
                                                "B3": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.5524
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L4": {{
                                                  "valueReference": "41"
                                                }},
                                                "B4": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.5741
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L5": {{
                                                  "valueReference": "53"
                                                }},
                                                "B5": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.3124
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L6": {{
                                                  "valueReference": "54"
                                                }},
                                                "B6": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.2303
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }}
                                              }},
                                              "functionReference": "55"
                                            }}
                                          }},
                                          "names": {{
                                            "constantValue": [
                                              "BRIGHTNESS"
                                            ]
                                          }}
                                        }},
                                        "functionName": "Image.rename"
                                      }}
                                    }},
                                    "srcImg": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "DEFAULT_EXPRESSION_IMAGE": {{
                                                  "argumentReference": "_MAPPING_VAR_0_0"
                                                }},
                                                "L1": {{
                                                  "valueReference": "44"
                                                }},
                                                "B1": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": -0.1603
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L2": {{
                                                  "valueReference": "52"
                                                }},
                                                "B2": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": -0.2819
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L3": {{
                                                  "valueReference": "42"
                                                }},
                                                "B3": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": -0.4934
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L4": {{
                                                  "valueReference": "41"
                                                }},
                                                "B4": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.794
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L5": {{
                                                  "valueReference": "53"
                                                }},
                                                "B5": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": -0.0002
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L6": {{
                                                  "valueReference": "54"
                                                }},
                                                "B6": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": -0.1446
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }}
                                              }},
                                              "functionReference": "55"
                                            }}
                                          }},
                                          "names": {{
                                            "constantValue": [
                                              "GREENNESS"
                                            ]
                                          }}
                                        }},
                                        "functionName": "Image.rename"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Image.addBands"
                                }}
                              }},
                              "srcImg": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "DEFAULT_EXPRESSION_IMAGE": {{
                                            "argumentReference": "_MAPPING_VAR_0_0"
                                          }},
                                          "L1": {{
                                            "valueReference": "44"
                                          }},
                                          "B1": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": 0.0315
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }},
                                          "L2": {{
                                            "valueReference": "52"
                                          }},
                                          "B2": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": 0.2021
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }},
                                          "L3": {{
                                            "valueReference": "42"
                                          }},
                                          "B3": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": 0.3102
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }},
                                          "L4": {{
                                            "valueReference": "41"
                                          }},
                                          "B4": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": 0.1594
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }},
                                          "L5": {{
                                            "valueReference": "53"
                                          }},
                                          "B5": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": -0.6806
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }},
                                          "L6": {{
                                            "valueReference": "54"
                                          }},
                                          "B6": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": -0.6109
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }}
                                        }},
                                        "functionReference": "55"
                                      }}
                                    }},
                                    "names": {{
                                      "constantValue": [
                                        "WETNESS"
                                      ]
                                    }}
                                  }},
                                  "functionName": "Image.rename"
                                }}
                              }}
                            }},
                            "functionName": "Image.addBands"
                          }}
                        }}
                      }},
                      "functionName": "Image.addBands"
                    }}
                  }},
                  "srcImg": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "input": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "dstImg": {{
                                            "valueReference": "56"
                                          }},
                                          "srcImg": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "input": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "DEFAULT_EXPRESSION_IMAGE": {{
                                                        "valueReference": "57"
                                                      }},
                                                      "GV": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "input": {{
                                                              "valueReference": "57"
                                                            }},
                                                            "bandSelectors": {{
                                                              "arrayValue": {{
                                                                "values": [
                                                                  {{
                                                                    "valueReference": "58"
                                                                  }}
                                                                ]
                                                              }}
                                                            }}
                                                          }},
                                                          "functionName": "Image.select"
                                                        }}
                                                      }},
                                                      "SHADE": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "input": {{
                                                              "valueReference": "57"
                                                            }},
                                                            "bandSelectors": {{
                                                              "arrayValue": {{
                                                                "values": [
                                                                  {{
                                                                    "valueReference": "59"
                                                                  }}
                                                                ]
                                                              }}
                                                            }}
                                                          }},
                                                          "functionName": "Image.select"
                                                        }}
                                                      }},
                                                      "NPV": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "input": {{
                                                              "valueReference": "57"
                                                            }},
                                                            "bandSelectors": {{
                                                              "arrayValue": {{
                                                                "values": [
                                                                  {{
                                                                    "valueReference": "60"
                                                                  }}
                                                                ]
                                                              }}
                                                            }}
                                                          }},
                                                          "functionName": "Image.select"
                                                        }}
                                                      }},
                                                      "SOIL": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "input": {{
                                                              "valueReference": "57"
                                                            }},
                                                            "bandSelectors": {{
                                                              "arrayValue": {{
                                                                "values": [
                                                                  {{
                                                                    "valueReference": "61"
                                                                  }}
                                                                ]
                                                              }}
                                                            }}
                                                          }},
                                                          "functionName": "Image.select"
                                                        }}
                                                      }}
                                                    }},
                                                    "functionReference": "63"
                                                  }}
                                                }},
                                                "names": {{
                                                  "arrayValue": {{
                                                    "values": [
                                                      {{
                                                        "valueReference": "66"
                                                      }}
                                                    ]
                                                  }}
                                                }}
                                              }},
                                              "functionName": "Image.rename"
                                            }}
                                          }}
                                        }},
                                        "functionName": "Image.addBands"
                                      }}
                                    }},
                                    "bandSelectors": {{
                                      "arrayValue": {{
                                        "values": [
                                          {{
                                            "valueReference": "58"
                                          }},
                                          {{
                                            "valueReference": "59"
                                          }},
                                          {{
                                            "valueReference": "60"
                                          }},
                                          {{
                                            "valueReference": "61"
                                          }},
                                          {{
                                            "valueReference": "66"
                                          }}
                                        ]
                                      }}
                                    }}
                                  }},
                                  "functionName": "Image.select"
                                }}
                              }},
                              "names": {{
                                "arrayValue": {{
                                  "values": [
                                    {{
                                      "valueReference": "64"
                                    }},
                                    {{
                                      "constantValue": "Shade"
                                    }},
                                    {{
                                      "valueReference": "65"
                                    }},
                                    {{
                                      "constantValue": "Soil"
                                    }},
                                    {{
                                      "valueReference": "66"
                                    }}
                                  ]
                                }}
                              }}
                            }},
                            "functionName": "Image.rename"
                          }}
                        }},
                        "mask": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "valueReference": "56"
                                    }},
                                    "bandSelectors": {{
                                      "arrayValue": {{
                                        "values": [
                                          {{
                                            "valueReference": "62"
                                          }}
                                        ]
                                      }}
                                    }}
                                  }},
                                  "functionName": "Image.select"
                                }}
                              }},
                              "image2": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "value": {{
                                      "constantValue": 0.1
                                    }}
                                  }},
                                  "functionName": "Image.constant"
                                }}
                              }}
                            }},
                            "functionName": "Image.lt"
                          }}
                        }}
                      }},
                      "functionName": "Image.updateMask"
                    }}
                  }}
                }},
                "functionName": "Image.addBands"
              }}
            }}
          }},
          "functionName": "Image.addBands"
        }}
      }},
      "41": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "21"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "42": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "valueReference": "43"
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "43": {{
        "arrayValue": {{
          "values": [
            {{
              "valueReference": "20"
            }}
          ]
        }}
      }},
      "44": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "18"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "45": {{
        "functionInvocationValue": {{
          "arguments": {{
            "expression": {{
              "constantValue": "float(2.5*(((B4) - (B3)) / ((B4) + (6 * (B3)) - (7.5 * (B1)) + 1)))"
            }},
            "argName": {{
              "valueReference": "46"
            }},
            "vars": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "47"
                  }},
                  {{
                    "valueReference": "48"
                  }},
                  {{
                    "valueReference": "49"
                  }},
                  {{
                    "valueReference": "50"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.parseExpression"
        }}
      }},
      "46": {{
        "valueReference": "47"
      }},
      "47": {{
        "constantValue": "DEFAULT_EXPRESSION_IMAGE"
      }},
      "48": {{
        "constantValue": "B4"
      }},
      "49": {{
        "constantValue": "B3"
      }},
      "50": {{
        "constantValue": "B1"
      }},
      "51": {{
        "functionInvocationValue": {{
          "arguments": {{
            "expression": {{
              "constantValue": "float(2.5*(((B4) - (B3)) / ((B4) + (2.4 * (B3)) + 1)))"
            }},
            "argName": {{
              "valueReference": "46"
            }},
            "vars": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "47"
                  }},
                  {{
                    "valueReference": "48"
                  }},
                  {{
                    "valueReference": "49"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.parseExpression"
        }}
      }},
      "52": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "19"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "53": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "22"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "54": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "23"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "55": {{
        "functionInvocationValue": {{
          "arguments": {{
            "expression": {{
              "constantValue": "(L1 * B1) + (L2 * B2) + (L3 * B3) + (L4 * B4) + (L5 * B5) + (L6 * B6)"
            }},
            "argName": {{
              "valueReference": "46"
            }},
            "vars": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "47"
                  }},
                  {{
                    "constantValue": "L1"
                  }},
                  {{
                    "valueReference": "50"
                  }},
                  {{
                    "constantValue": "L2"
                  }},
                  {{
                    "constantValue": "B2"
                  }},
                  {{
                    "constantValue": "L3"
                  }},
                  {{
                    "valueReference": "49"
                  }},
                  {{
                    "constantValue": "L4"
                  }},
                  {{
                    "valueReference": "48"
                  }},
                  {{
                    "constantValue": "L5"
                  }},
                  {{
                    "constantValue": "B5"
                  }},
                  {{
                    "constantValue": "L6"
                  }},
                  {{
                    "constantValue": "B6"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.parseExpression"
        }}
      }},
      "56": {{
        "functionInvocationValue": {{
          "arguments": {{
            "dstImg": {{
              "valueReference": "39"
            }},
            "srcImg": {{
              "valueReference": "57"
            }}
          }},
          "functionName": "Image.addBands"
        }}
      }},
      "57": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "image": {{
                    "valueReference": "39"
                  }},
                  "endmembers": {{
                    "constantValue": [
                      [
                        0.05,
                        0.09,
                        0.04,
                        0.61,
                        0.3,
                        0.1
                      ],
                      [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                      ],
                      [
                        0.14,
                        0.17,
                        0.22,
                        0.3,
                        0.55,
                        0.3
                      ],
                      [
                        0.2,
                        0.3,
                        0.34,
                        0.58,
                        0.6,
                        0.58
                      ],
                      [
                        0.9,
                        0.96,
                        0.8,
                        0.78,
                        0.72,
                        0.65
                      ]
                    ]
                  }},
                  "sumToOne": {{
                    "constantValue": true
                  }},
                  "nonNegative": {{
                    "constantValue": true
                  }}
                }},
                "functionName": "Image.unmix"
              }}
            }},
            "names": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "58"
                  }},
                  {{
                    "valueReference": "59"
                  }},
                  {{
                    "valueReference": "60"
                  }},
                  {{
                    "valueReference": "61"
                  }},
                  {{
                    "valueReference": "62"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.rename"
        }}
      }},
      "58": {{
        "constantValue": "band_0"
      }},
      "59": {{
        "constantValue": "band_1"
      }},
      "60": {{
        "constantValue": "band_2"
      }},
      "61": {{
        "constantValue": "band_3"
      }},
      "62": {{
        "constantValue": "band_4"
      }},
      "63": {{
        "functionInvocationValue": {{
          "arguments": {{
            "expression": {{
              "constantValue": "((GV / (1 - SHADE)) - (NPV + SOIL)) / ((GV / (1 - SHADE)) + NPV + SOIL)"
            }},
            "argName": {{
              "valueReference": "46"
            }},
            "vars": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "47"
                  }},
                  {{
                    "valueReference": "64"
                  }},
                  {{
                    "constantValue": "SHADE"
                  }},
                  {{
                    "valueReference": "65"
                  }},
                  {{
                    "constantValue": "SOIL"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.parseExpression"
        }}
      }},
      "64": {{
        "constantValue": "GV"
      }},
      "65": {{
        "constantValue": "NPV"
      }},
      "66": {{
        "constantValue": "NDFI"
      }},
      "67": {{
        "constantValue": "year"
      }},
      "68": {{
        "functionInvocationValue": {{
          "arguments": {{
            "date": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "year": {{
                    "valueReference": "69"
                  }},
                  "month": {{
                    "valueReference": "70"
                  }},
                  "day": {{
                    "valueReference": "70"
                  }}
                }},
                "functionName": "Date.fromYMD"
              }}
            }},
            "delta": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "left": {{
                    "argumentReference": "_MAPPING_VAR_0_0"
                  }},
                  "right": {{
                    "valueReference": "69"
                  }}
                }},
                "functionName": "Number.subtract"
              }}
            }},
            "unit": {{
              "valueReference": "67"
            }}
          }},
          "functionName": "Date.advance"
        }}
      }},
      "69": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }}
          }},
          "functionName": "Number.floor"
        }}
      }},
      "70": {{
        "constantValue": 1
      }},
      "71": {{
        "functionInvocationValue": {{
          "arguments": {{
            "object": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "input": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image": {{
                          "valueReference": "27"
                        }},
                        "mask": {{
                          "valueReference": "27"
                        }}
                      }},
                      "functionName": "Image.mask"
                    }}
                  }},
                  "names": {{
                    "valueReference": "43"
                  }}
                }},
                "functionName": "Image.rename"
              }}
            }},
            "key": {{
              "valueReference": "38"
            }},
            "value": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "date": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "value": {{
                          "argumentReference": "_MAPPING_VAR_0_0"
                        }}
                      }},
                      "functionName": "Date"
                    }}
                  }}
                }},
                "functionName": "Date.millis"
              }}
            }}
          }},
          "functionName": "Element.set"
        }}
      }},
      "72": {{
        "functionInvocationValue": {{
          "arguments": {{
            "object": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "object": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "object": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "object": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "object": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "object": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "object": {{
                                                  "argumentReference": "_MAPPING_VAR_4_0"
                                                }},
                                                "key": {{
                                                  "valueReference": "73"
                                                }},
                                                "value": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "dictionary": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "image": {{
                                                              "functionInvocationValue": {{
                                                                "arguments": {{
                                                                  "input": {{
                                                                    "argumentReference": "_MAPPING_VAR_4_0"
                                                                  }},
                                                                  "bandSelectors": {{
                                                                    "valueReference": "43"
                                                                  }}
                                                                }},
                                                                "functionName": "Image.select"
                                                              }}
                                                            }},
                                                            "reducer": {{
                                                              "valueReference": "74"
                                                            }},
                                                            "geometry": {{
                                                              "valueReference": "5"
                                                            }},
                                                            "crs": {{
                                                              "valueReference": "75"
                                                            }}
                                                          }},
                                                          "functionName": "Image.reduceRegion"
                                                        }}
                                                      }},
                                                      "key": {{
                                                        "valueReference": "20"
                                                      }}
                                                    }},
                                                    "functionName": "Dictionary.getNumber"
                                                  }}
                                                }}
                                              }},
                                              "functionName": "Element.set"
                                            }}
                                          }},
                                          "key": {{
                                            "constantValue": "fitTime"
                                          }},
                                          "value": {{
                                            "valueReference": "76"
                                          }}
                                        }},
                                        "functionName": "Element.set"
                                      }}
                                    }},
                                    "key": {{
                                      "valueReference": "79"
                                    }},
                                    "value": {{
                                      "valueReference": "80"
                                    }}
                                  }},
                                  "functionName": "Element.set"
                                }}
                              }},
                              "key": {{
                                "constantValue": "coef"
                              }},
                              "value": {{
                                "valueReference": "82"
                              }}
                            }},
                            "functionName": "Element.set"
                          }}
                        }},
                        "key": {{
                          "constantValue": "segment"
                        }},
                        "value": {{
                          "valueReference": "84"
                        }}
                      }},
                      "functionName": "Element.set"
                    }}
                  }},
                  "key": {{
                    "valueReference": "91"
                  }},
                  "value": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "date": {{
                          "valueReference": "78"
                        }},
                        "format": {{
                          "constantValue": "YYYY-MM-dd"
                        }}
                      }},
                      "functionName": "Date.format"
                    }}
                  }}
                }},
                "functionName": "Element.set"
              }}
            }},
            "key": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "number": {{
                    "valueReference": "84"
                  }},
                  "pattern": {{
                    "constantValue": "h%d"
                  }}
                }},
                "functionName": "Number.format"
              }}
            }},
            "value": {{
              "valueReference": "80"
            }}
          }},
          "functionName": "Element.set"
        }}
      }},
      "73": {{
        "constantValue": "value"
      }},
      "74": {{
        "functionInvocationValue": {{
          "arguments": {{}},
          "functionName": "Reducer.first"
        }}
      }},
      "75": {{
        "functionInvocationValue": {{
          "arguments": {{
            "projection": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "crs": {{
                    "constantValue": "EPSG:4326"
                  }}
                }},
                "functionName": "Projection"
              }}
            }},
            "meters": {{
              "constantValue": 30
            }}
          }},
          "functionName": "Projection.atScale"
        }}
      }},
      "76": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "valueReference": "77"
            }},
            "right": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "date": {{
                    "valueReference": "78"
                  }},
                  "start": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "year": {{
                          "valueReference": "77"
                        }},
                        "month": {{
                          "valueReference": "70"
                        }},
                        "day": {{
                          "valueReference": "70"
                        }}
                      }},
                      "functionName": "Date.fromYMD"
                    }}
                  }},
                  "unit": {{
                    "valueReference": "67"
                  }}
                }},
                "functionName": "Date.difference"
              }}
            }}
          }},
          "functionName": "Number.add"
        }}
      }},
      "77": {{
        "functionInvocationValue": {{
          "arguments": {{
            "date": {{
              "valueReference": "78"
            }},
            "unit": {{
              "valueReference": "67"
            }}
          }},
          "functionName": "Date.get"
        }}
      }},
      "78": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image": {{
              "argumentReference": "_MAPPING_VAR_4_0"
            }}
          }},
          "functionName": "Image.date"
        }}
      }},
      "79": {{
        "constantValue": "fit"
      }},
      "80": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "left": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "left": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "left": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "left": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "left": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "left": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "array": {{
                                                        "valueReference": "81"
                                                      }},
                                                      "position": {{
                                                        "constantValue": [
                                                          0
                                                        ]
                                                      }}
                                                    }},
                                                    "functionName": "Array.get"
                                                  }}
                                                }},
                                                "right": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "left": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "array": {{
                                                              "valueReference": "81"
                                                            }},
                                                            "position": {{
                                                              "valueReference": "87"
                                                            }}
                                                          }},
                                                          "functionName": "Array.get"
                                                        }}
                                                      }},
                                                      "right": {{
                                                        "valueReference": "76"
                                                      }}
                                                    }},
                                                    "functionName": "Number.multiply"
                                                  }}
                                                }}
                                              }},
                                              "functionName": "Number.add"
                                            }}
                                          }},
                                          "right": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "left": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "array": {{
                                                        "valueReference": "81"
                                                      }},
                                                      "position": {{
                                                        "constantValue": [
                                                          2
                                                        ]
                                                      }}
                                                    }},
                                                    "functionName": "Array.get"
                                                  }}
                                                }},
                                                "right": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "input": {{
                                                        "valueReference": "88"
                                                      }}
                                                    }},
                                                    "functionName": "Number.cos"
                                                  }}
                                                }}
                                              }},
                                              "functionName": "Number.multiply"
                                            }}
                                          }}
                                        }},
                                        "functionName": "Number.add"
                                      }}
                                    }},
                                    "right": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "left": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "array": {{
                                                  "valueReference": "81"
                                                }},
                                                "position": {{
                                                  "constantValue": [
                                                    3
                                                  ]
                                                }}
                                              }},
                                              "functionName": "Array.get"
                                            }}
                                          }},
                                          "right": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "input": {{
                                                  "valueReference": "88"
                                                }}
                                              }},
                                              "functionName": "Number.sin"
                                            }}
                                          }}
                                        }},
                                        "functionName": "Number.multiply"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Number.add"
                                }}
                              }},
                              "right": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "left": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "array": {{
                                            "valueReference": "81"
                                          }},
                                          "position": {{
                                            "constantValue": [
                                              4
                                            ]
                                          }}
                                        }},
                                        "functionName": "Array.get"
                                      }}
                                    }},
                                    "right": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "valueReference": "89"
                                          }}
                                        }},
                                        "functionName": "Number.cos"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Number.multiply"
                                }}
                              }}
                            }},
                            "functionName": "Number.add"
                          }}
                        }},
                        "right": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "left": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "array": {{
                                      "valueReference": "81"
                                    }},
                                    "position": {{
                                      "constantValue": [
                                        5
                                      ]
                                    }}
                                  }},
                                  "functionName": "Array.get"
                                }}
                              }},
                              "right": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "valueReference": "89"
                                    }}
                                  }},
                                  "functionName": "Number.sin"
                                }}
                              }}
                            }},
                            "functionName": "Number.multiply"
                          }}
                        }}
                      }},
                      "functionName": "Number.add"
                    }}
                  }},
                  "right": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "left": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "array": {{
                                "valueReference": "81"
                              }},
                              "position": {{
                                "constantValue": [
                                  6
                                ]
                              }}
                            }},
                            "functionName": "Array.get"
                          }}
                        }},
                        "right": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "input": {{
                                "valueReference": "90"
                              }}
                            }},
                            "functionName": "Number.cos"
                          }}
                        }}
                      }},
                      "functionName": "Number.multiply"
                    }}
                  }}
                }},
                "functionName": "Number.add"
              }}
            }},
            "right": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "left": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "array": {{
                          "valueReference": "81"
                        }},
                        "position": {{
                          "constantValue": [
                            7
                          ]
                        }}
                      }},
                      "functionName": "Array.get"
                    }}
                  }},
                  "right": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "input": {{
                          "valueReference": "90"
                        }}
                      }},
                      "functionName": "Number.sin"
                    }}
                  }}
                }},
                "functionName": "Number.multiply"
              }}
            }}
          }},
          "functionName": "Number.add"
        }}
      }},
      "81": {{
        "functionInvocationValue": {{
          "arguments": {{
            "values": {{
              "valueReference": "82"
            }}
          }},
          "functionName": "Array"
        }}
      }},
      "82": {{
        "functionInvocationValue": {{
          "arguments": {{
            "condition": {{
              "valueReference": "83"
            }},
            "trueCase": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "array": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "array": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "dictionary": {{
                                "valueReference": "85"
                              }},
                              "key": {{
                                "constantValue": "RED_coefs"
                              }}
                            }},
                            "functionName": "Dictionary.getArray"
                          }}
                        }},
                        "axis": {{
                          "constantValue": 0
                        }},
                        "start": {{
                          "valueReference": "84"
                        }},
                        "end": {{
                          "valueReference": "83"
                        }}
                      }},
                      "functionName": "Array.slice"
                    }}
                  }},
                  "axes": {{
                    "valueReference": "87"
                  }}
                }},
                "functionName": "Array.project"
              }}
            }},
            "falseCase": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "values": {{
                    "constantValue": [
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0
                    ]
                  }}
                }},
                "functionName": "Array"
              }}
            }}
          }},
          "functionName": "If"
        }}
      }},
      "83": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "valueReference": "84"
            }},
            "right": {{
              "valueReference": "70"
            }}
          }},
          "functionName": "Number.add"
        }}
      }},
      "84": {{
        "functionInvocationValue": {{
          "arguments": {{
            "list": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "array": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "left": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "left": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "values": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "dictionary": {{
                                            "valueReference": "85"
                                          }},
                                          "key": {{
                                            "constantValue": "tStart"
                                          }}
                                        }},
                                        "functionName": "Dictionary.get"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Array"
                                }}
                              }},
                              "right": {{
                                "valueReference": "86"
                              }}
                            }},
                            "functionName": "Array.lte"
                          }}
                        }},
                        "right": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "left": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "values": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "dictionary": {{
                                            "valueReference": "85"
                                          }},
                                          "key": {{
                                            "constantValue": "tEnd"
                                          }}
                                        }},
                                        "functionName": "Dictionary.get"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Array"
                                }}
                              }},
                              "right": {{
                                "valueReference": "86"
                              }}
                            }},
                            "functionName": "Array.gte"
                          }}
                        }}
                      }},
                      "functionName": "Array.and"
                    }}
                  }}
                }},
                "functionName": "Array.toList"
              }}
            }},
            "element": {{
              "constantValue": 1
            }}
          }},
          "functionName": "List.indexOf"
        }}
      }},
      "85": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "collection": {{
                    "valueReference": "2"
                  }},
                  "breakpointBands": {{
                    "arrayValue": {{
                      "values": [
                        {{
                          "valueReference": "19"
                        }},
                        {{
                          "valueReference": "20"
                        }},
                        {{
                          "valueReference": "21"
                        }},
                        {{
                          "valueReference": "22"
                        }},
                        {{
                          "valueReference": "23"
                        }}
                      ]
                    }}
                  }},
                  "tmaskBands": {{
                    "arrayValue": {{
                      "values": [
                        {{
                          "valueReference": "19"
                        }},
                        {{
                          "valueReference": "23"
                        }}
                      ]
                    }}
                  }},
                  "minObservations": {{
                    "constantValue": 6
                  }},
                  "chiSquareProbability": {{
                    "constantValue": 0.99
                  }},
                  "minNumOfYearsScaler": {{
                    "constantValue": 1.33
                  }},
                  "dateFormat": {{
                    "valueReference": "70"
                  }},
                  "lambda": {{
                    "constantValue": 0.002
                  }},
                  "maxIterations": {{
                    "constantValue": 10000
                  }}
                }},
                "functionName": "TemporalSegmentation.Ccdc"
              }}
            }},
            "reducer": {{
              "valueReference": "74"
            }},
            "geometry": {{
              "valueReference": "5"
            }},
            "crs": {{
              "valueReference": "75"
            }}
          }},
          "functionName": "Image.reduceRegion"
        }}
      }},
      "86": {{
        "functionInvocationValue": {{
          "arguments": {{
            "values": {{
              "valueReference": "76"
            }}
          }},
          "functionName": "Array"
        }}
      }},
      "87": {{
        "constantValue": [
          1
        ]
      }},
      "88": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "valueReference": "76"
            }},
            "right": {{
              "constantValue": 6.283185307179586
            }}
          }},
          "functionName": "Number.multiply"
        }}
      }},
      "89": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "valueReference": "76"
            }},
            "right": {{
              "constantValue": 12.566370614359172
            }}
          }},
          "functionName": "Number.multiply"
        }}
      }},
      "90": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "valueReference": "76"
            }},
            "right": {{
              "constantValue": 18.84955592153876
            }}
          }},
          "functionName": "Number.multiply"
        }}
      }},
      "91": {{
        "constantValue": "dateString"
      }},
      "92": {{
        "constantValue": 9
      }}
    }}
  }}
}}"""
